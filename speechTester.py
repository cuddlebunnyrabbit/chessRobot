import speech_recognition as sr #pip3 install SpeechRecognition

#from pocketsphinx import LiveSpeech 
'''
for phrase in LiveSpeech():
    print(phrase)
'''

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Speak Anything:')
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)#convert audio to text
        print('You said: {}'.format(text))

    except:
        print('Sorry could not recognize your voice')
