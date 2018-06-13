#!/usr/bin/python
import datetime
import pyttsx
import os
import weather



# function to fulfill required job
def task():
    global output
    output = None

    if job == 1:
        output = 'Good day sir!'
        speak()
        exit()

    elif job == 2:

        output = 'The time is ' + datetime.datetime.now().strftime("%I:%M %p")

    elif job == 3:

        output = 'The date is, ' + datetime.datetime.now().strftime("%a, %B %d %Y")

    elif job == 4:

        os.system("python ./games/rpg.py")
        output = 'I hope that was fun.'
    
    elif job == 5:
        from weather import Weather, Unit

        weather = Weather(unit=Unit.FAHRENHEIT)
        location = weather.lookup_by_location('logan,ohio')
        condition = location.condition
        output = 'The forcast for today is ' + condition.text

    elif job == 0:

        output = "I didn't understand that."

    return;

# function to get input and process
def ginput ():

    global job
    job = None
    # Ask for input
    command = raw_input('|-|=> ').lower() 

    # Process Input
    commStr = command.split(" ")

    if "exit" in commStr:

        job = 1

    elif "time" in commStr:
       
        job = 2 

    elif "date" in commStr:

        job = 3
 

    elif "play" in commStr:
        if "rpg" in commStr:
            job = 4
        else:
            job = 0

       
    elif "weather" in commStr:

        job = 5            

    else:
        job = 0
    #print "You Asked for:", commStr[1]

    return;

def speak ():
    engine = pyttsx.init()
    engine.say(output)
    a = engine.runAndWait()
    return;

flag = 1

# Function Calls
while flag == 1:
    ginput()
    task()
    #print output
    speak()
    
    