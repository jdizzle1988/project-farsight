#!/usr/bin/python
import pyttsx

def speak ():
    engine = pyttsx.init()
    engine.say(output)
    a = engine.runAndWait()
    return;



def start ():
    global output
    output = None

    output = 'You are about to embark on a mystic journey through the world.'
    speak()
    output = 'Tell me your name, brave adventurer.'
    speak()
    resp = raw_input('|-|=> ').lower()
    output = 'Hello ' + resp
    speak()
    return;


start()

print "RPG End"