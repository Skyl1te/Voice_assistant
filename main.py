from functions import *
from pyfiglet import Figlet
from colorama import init, Fore
init()

preview_text = Figlet(font='slant')
print(Fore.RED + preview_text.renderText('Voice assistant'))

#Your microphone index
# import speech_recognition as sr
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)



