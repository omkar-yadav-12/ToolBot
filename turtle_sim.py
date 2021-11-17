import turtle
import time
import speech_recognition as sr
import math
from difflib import SequenceMatcher

tools = ["HAMMER", "WRENCH", "SCREWDRIVER", "DRILL"]
toolPos = [[-5,-220], [-10,-185],[-22,-140],[-60,-82]]
r = sr.Recognizer()
r.energy_threshold = 300
activated = False
def activate_toolbot():
    print("Toolbot activated")
    #activated = True
    #some function to activate lights and play a sound on RPi
    
    with sr.Microphone() as source:
        print("Listening for tool")
        tool_requested = r.listen(source)
        print("End")
        try:
            sentence = r.recognize_google(tool_requested).upper()
            print(sentence)
            for t in tools:
                if t in sentence:
                    get_tool(t)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
def checkForTool(s):
    for t in tools:
        if t in s.upper():
            get_tool(t)
            return -1
    return 0
def get_tool(tool):
    print("Getting " + tool)
    toolNum = tools.index(tool)
    print(tool + " in row " + str(toolNum))
    #actually get the tool assuming we are starting from 0,0
    deg = math.atan2(toolPos[toolNum][1],toolPos[toolNum][0]) * 180 / math.pi
    bot.setheading(deg)
    bot.setpos(toolPos[toolNum][0], toolPos[toolNum][1])
    bot.setheading(180)
    time.sleep(1)
    bot.setheading(deg-180)
    bot.setpos(0,0)
    deliver_tool()

def deliver_tool():
    deg = math.atan2(130,-130)
    bot.setheading(deg)
    bot.setpos(-130, 130)
    bot.setheading(90)
    time.sleep(1)
    return_to_base()
def return_to_base():
    deg = math.atan2(-bot.xcor(), -bot.ycor())      
    bot.setheading(deg)        
    bot.setpos(0,0)
    bot.setheading(90)
wn = turtle.Screen()
#wn.screensize(400,400, "white")
wn.bgpic("lab_gif.gif")
wn.title("ToolBot")

homeBase = turtle.Turtle()
homeBase.shape("circle")
homeBase.color("yellow")
homeBase.resizemode("user")
homeBase.turtlesize(1.5, 1.5, 1)
bot = turtle.Turtle()
bot.shape("triangle")
bot.color("blue")
bot.up()
bot.speed(1)
human = turtle.Turtle()
human.hideturtle()
human.shape("square")
human.color("red")
human.up()
human.setpos(-135,160)
human.showturtle()
with sr.Microphone() as source:
    while True:
        #time.sleep(2)
        #bot.forward(25)
    
        print("Start")
        audio = r.listen(source)
        print("End")

        trigger_word = "toolbox"

        try:
            text = r.recognize_google(audio)#.upper()
            trigger_text = "HEY TOOLBOT"
            print(text)        
            if (trigger_word.lower() in text.lower() or "tool bot" in text.lower() or "tool box" in text.lower()):
                if(checkForTool(text) == 0):
                    activate_toolbot()

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
#wn.mainloop()