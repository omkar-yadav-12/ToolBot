import speech_recognition as sr

#Speech Recognition Guides
#https://realpython.com/python-speech-recognition/
#https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/

r = sr.Recognizer()

aFile = sr.AudioFile("gettysburg10.wav")

with aFile as source:
    audio = r.record(source)

try:
    print(r.recognize_google(audio))

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
  
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))