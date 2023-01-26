import os
import re
import data.voice as tts

def loadCommands():
    commands = []
    for command in os.listdir("./commands"):
        if command.endswith(".py"):
            name = command[:-3]
            try:
                commands.append(__import__("commands." + name, fromlist = [name]))
            except Exception as e:
                print("Error loading command " + name + ": " + str(e))
    return commands


def checkCommands(engine, voice):
    voice = voice.lower()
    commands = loadCommands()
    for command in commands:
        command = command.Command()
        i = 0
        for alias in command.data['aliases']:
            if re.match(alias, voice):
                if ".+" in alias:
                    fluff = alias.split(".+")
                    if len(fluff[1]) == 0:
                        voice = voice[len(fluff[0]):]
                    elif len(fluff) > 1:
                        voice = voice[len(fluff[0]):]
                        voice = voice[:-len(fluff[1])]
                    output = command.run(i, voice)
                    if output != None:
                        tts.say(engine, output)
                else:
                    output = command.run(i)
                    if output != None:
                        tts.say(engine, output)
                return True
            i += 1
    return False