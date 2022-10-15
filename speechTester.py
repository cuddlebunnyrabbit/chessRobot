import speech_recognition as sr
from pocketsphinx import LiveSpeech

for phrase in LiveSpeech():
    print(phrase)
