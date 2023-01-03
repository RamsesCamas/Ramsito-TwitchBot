import os
from twitchio.ext import commands
from dotenv import load_dotenv
import random

load_dotenv()


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
        await self.handle_commands(message)
        ctx = commands.Context(message,self)
        if 'chiste' in message.content.lower() and 'Ramsito' in message.content:
            await ctx.send(random.choice(CHISTES))
        else: await ctx.send("Ahorita te atiendo")
bot = Bot()
bot.run()
