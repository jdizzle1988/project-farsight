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
    global name
    name = resp
    output = 'Hello ' + resp
    speak()
    output = 'What kinda of class are you? Warrior, Mage, or Rogue?'
    speak()
    resp = raw_input('|-|=> ').lower()
    global clss
    clss = resp
    output = 'So ' + name + ', you are a ' + clss
    speak()
    if clss == 'warrior':
        output = 'Your starting inventory as a warrior is a rusty shortsword and a shield. You are wearing a chainmail shirt.'
        speak()
    elif clss == 'mage':
        ouput = 'Your starting inventory as a mage is an old staff and a spellbook. You are wearing a robe.'
        speak()
    elif clss == 'rogue':
        output = 'Your starting inventory as a rogue is two rusty daggers. You are wearing leather armor.'
        speak()
    return;

def game ():

    desc = 'So ' + name + 'You stand in an Inn. The obvious exits are, south. Which way would you like to go?'

    return;

def gen_room ():
        global exits
        exits = None
    return;

start()

print "RPG End"