import pyttsx3
import json
import time

engine = pyttsx3.init()

def say_something(words):
    engine.say(words)
    print(words)
    engine.runAndWait()

def countdown():
    say_something('five')
    time.sleep(1)
    say_something('four')
    time.sleep(1)
    say_something('three')
    time.sleep(1)
    say_something('two')
    time.sleep(1)
    say_something('one')
    time.sleep(1)

with open('tab.json','r') as f:
    file_read = f.read()
    info = json.loads(file_read)

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')
say_something("Welcome to tabbata")
time.sleep(1)
say_something("Lets start")

effort_time = info["times"]["effort"]
rest_time = info["times"]["rest"]


for exercise in info['exercises']:
    engine.setProperty('voice', '')
    say_something('Lets do {} for {}'.format(exercise, effort_time))
    if effort_time > 5:
        time.sleep(effort_time - 5)
        countdown()
    elif effort_time <= 5:
        time.sleep(effort_time)
    say_something("Rest now for {} seconds".format(rest_time))
    time.sleep(rest_time)

