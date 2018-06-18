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
    global desc 
    desc = None
    
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

    gen_room()
    output = name + ', ' + desc
    speak()

    return;

def gen_room ():
    
    exits = ['north', 'south', 'east', 'west']

    import numpy as nrand

    exit1 = exits[nrand.random.rand(3)]
    exit2 = exits[nrand.random.rand(3)]

    rtype = ['A dank brick room', 'A dimly lit room', 'A room full of bones', 'A room with an inch of water on the floor', 'A brightly lit room']

    room_type = rtype[nrand.random.rand(4)]
    
    desc = 'You enter into ' + room_type + ' the obvious exits are ' + exit1 + ' and ' + exit2

    return desc;

start()
game()

print "RPG End"