import os
from twitchio.ext import commands
from dotenv import load_dotenv
import random

from gtts import gTTS
from playsound import playsound

load_dotenv()

SOUND_FILE_NAME = 'RamsitoVoice.mp3'
#Sound files
HEY_HEY_FILE = 'HeyHey.wav'
GREETINGS_FILE = 'ohaiyoo.mp3'
STOP_FILE = 'YameteKudasai.wav'
BLESSING_FILE = 'bendicion.mp3'


def speak_from_text(text:str):
    tts = gTTS(text, lang="es")
    tts.save(SOUND_FILE_NAME)
    playsound(SOUND_FILE_NAME)
    os.remove(SOUND_FILE_NAME)

def play_file(filename):
    playsound(filename)

CHISTES = [
    'Hay tres tipos de personas en el mundo: los que saben contar y los que no.',
    '— Eres un fanático de la informática, ¿verdad? \n — Sí... mouse o menos.',
    '¿Cómo se llama un boomerang que no vuelve? \n Un palo.',
    '¿Cuál es el animal más tonto de la selva? El oso polar.',
    'Iba a contar un chiste sobre sodio... pero Na.'
]

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=os.environ['ACCESS_TOKEN'], prefix='Ramsito ', initial_channels=[os.environ['CHANNEL']])
    
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def hola(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hola {ctx.author.name}, eres un crack!')
        play_file(GREETINGS_FILE)
    
    @commands.command()
    async def detente(self, ctx: commands.Context):
        play_file(STOP_FILE)

    @commands.command()
    async def hey(self,ctx: commands.Context):
        await ctx.send("Ahorita le digo que les haga caso.")
        play_file(HEY_HEY_FILE)

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)
        #await commands.Context.send(self=commands.Context,content="Ahorita te atiendo")
        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        ctx = commands.Context(message,self)
        if 'Ramsito' in message.content:
            await self.handle_commands(message)
        else:
            if 'chiste' in message.content.lower():
                joke_to_tell = random.choice(CHISTES)
                await ctx.send(joke_to_tell)
                speak_from_text(joke_to_tell)
            elif any(nice_word  in message.content.lower() for nice_word in ['gusto','gustar','genial','nice']):
                play_file(BLESSING_FILE)
            else: 
                speak_from_text(f'Ahorita te atiendo {ctx.author.name}')
bot = Bot()
bot.run()
