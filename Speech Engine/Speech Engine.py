# Library

import speech_recognition as sr
import pyttsx3
import os

# Default

os.system('COLOR 0F')
os.system('CLS')

# Page Design

os.system('ECHO.')

engine = pyttsx3.init()
engine.say("Hiy. Select your theme. For Dark theme Enter D and For Light theme Enter L")
engine.runAndWait()

Design = str(input("..............(Hi \n..............(Select your theme <D>(Dark)/<L>(Light) | For example d: "))

o = False

match Design:
    case 'D':
        engine = pyttsx3.init()
        engine.say("Theme applied")
        engine.runAndWait()

        os.system('COLOR 0B')
        o = True
    case 'd':
        engine = pyttsx3.init()
        engine.say("Theme applied")
        engine.runAndWait()

        os.system('COLOR 0B')
        o = True
    case 'L':
        engine = pyttsx3.init()
        engine.say("Theme applied")
        engine.runAndWait()

        os.system('COLOR 50')
        o = True
    case 'l':
        engine = pyttsx3.init()
        engine.say("Theme applied")
        engine.runAndWait()

        os.system('COLOR 50')
        o = True

# Age

engine = pyttsx3.init()
engine.say("How Old Are You?")
engine.runAndWait()

os.system('CLS')
os.system('ECHO.')
Age = float(input("..............(How Old Are You?: "))

engine = pyttsx3.init()
engine.say("OK")
engine.runAndWait()

a = 0.0

try:
   a = float(Age)
except ValueError:
    os.system("CLS")
    os.system('ECHO.')
    print("............../ Oops! Not a number...")

    engine = pyttsx3.init()
    engine.say("Oops! Not a number")
    engine.runAndWait()

if a >= 18:
    b = True
    os.system("CLS")
    os.system('ECHO.')
    print("..............(Welcome!")

    engine = pyttsx3.init()
    engine.say("Welcome")
    engine.runAndWait()

else:
    b = False
    os.system("CLS")
    os.system('ECHO.')
    print("............../Sorry! ⛔ Access Denied... \n\n............../You Are Under 18 Years Of Age; Your Entry Is Prohibited!")

    engine = pyttsx3.init()
    engine.say("Sorry. Access Denied. You Are Under 18 Years Of Age; Your Entry Is Prohibited!")
    engine.runAndWait()

# Calculator

if b == True:
    os.system("CLS")

    engine = pyttsx3.init()
    engine.say("Enter First Number")
    engine.runAndWait()

    os.system('ECHO.')
    A = str(input("..............(Enter First Number: "))
    
    engine = pyttsx3.init()
    engine.say("OK")
    engine.runAndWait()

    engine = pyttsx3.init()
    engine.say("Enter Operator. Sum, Minus, Multiple, Exponent, Division, Addition, Divisor")
    engine.runAndWait()

    os.system('ECHO.')
    AB = str(input("..............(Enter Operator(Sum +|Minus -|Multiple *|Exponent **|Division /|Addition //|Divisor %): "))
    
    engine = pyttsx3.init()
    engine.say("OK")
    engine.runAndWait()

    engine = pyttsx3.init()
    engine.say("Enter Second Number")
    engine.runAndWait()

    os.system('ECHO.')
    B = str(input("..............(Enter Second Number: "))

    engine = pyttsx3.init()
    engine.say("OK")
    engine.runAndWait()

    g1 = 0.0
    g2 = 0.0
    h = True
    try:
        g1 = float(A)
        g2 = float(B)
    except ValueError:
        b == False
        os.system('CLS')
        os.system('ECHO.')
        print("............./ ⛔ Input number(s) or operator are not correct!")
        h == False

if h != False:
    R = 0.0
    match AB:
        case '+':
            R = g1+g2
        case '-':
            R = g1-g2
        case '*':
            R = g1*g2
        case '/':
            R = g1/g2
        case '**':
            R = g1**g2
        case '//':
            R = g1//g2
        case '%':
            R = g1%g2
if b == True:
    os.system('CLS')
    os.system('ECHO.')
    print("..............(Result: " + str(R))

    engine = pyttsx3.init()
    engine.say("Your result is: " + str(R))
    engine.runAndWait()