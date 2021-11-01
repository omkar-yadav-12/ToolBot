import speech_recognition as sr
from difflib import SequenceMatcher

#idk this might be helpful
#https://stackoverflow.com/questions/25394329/python-voice-recognition-library-always-listen

#array of available tools
tools = ["HAMMER", "WRENCH", "SCREWDRIVER", "DRILL"]
r = sr.Recognizer()
r.energy_threshold = 250

def activate_toolbot():
    print("Toolbot activated")
    #some function to activate lights and play a sound on RPi
    
    with sr.Microphone(3) as source:
        tool_requested = r.listen(source)

        try:
            tool = r.recognize_google(tool_requested).upper()
            if tool in tools:
                get_tool(tool)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def get_tool(tool):
    print("Getting " + tool)
    print(tool + " in row " + tools.index(tool))
    #actually get the tool

def main():
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)

        while True:
            print("Start")
            audio = r.listen(source)
            print("End")

            trigger_word = "toolbox"

            try:
                text = r.recognize_google(audio).upper()
                trigger_text = "HEY TOOLBOT"
                print(text)
                
                if (trigger_word.lower() in text.lower()):
                    activate_toolbot()

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    main()