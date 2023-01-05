from gtts import gTTS
from io import BytesIO
from playsound import playsound
import os

SOUND_FILE_NAME = 'HeyHey.wav'

if __name__ == '__main__':
    #tts = gTTS("Hola Mundo", lang="es")
    #tts.save(SOUND_FILE_NAME)
    #playsound(SOUND_FILE_NAME)
    playsound(SOUND_FILE_NAME)
    #os.remove(SOUND_FILE_NAME)