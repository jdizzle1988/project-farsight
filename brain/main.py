#!/usr/bin/python
import datetime
import pyttsx



# function to fulfill required job
def task():
    global output
    output = None

    if job == 1:
        
        output = 'The time is ' + datetime.datetime.now().strftime("%I:%M %p")

    elif job == 2:

        output = 'The date is, ' + datetime.datetime.now().strftime("%a, %B %d %Y")
    
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

    if "time" in commStr:
        
        job = 1 

    elif "date" in commStr:

        job = 2

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
    
    