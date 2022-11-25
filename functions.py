from libraries import *


def listen_command():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print('Say the command: ')
        audio = r.listen(source)

    try:
        our_speech = r.recognize_google(audio, language='en')
        print('You said: '+ our_speech)
        return our_speech
    except sr.UnknownValueError:
        return 'error'
    except sr.RequestError:
        return 'error'


def do_this_command(message):
    message = message.lower()
    if 'create' in message and 'text' in message or 'create' in message and 'txt' in message:
        say_message('One minute pls')
        Textfile  = open('_textFile_' + str(time()) + '.txt', 'w')
        Textfile.write('The file created')
        Textfile.close()
        say_message('The file was created')

    elif 'create' in message and 'HTML' in message or 'create' in message and 'html' in message:
        say_message('One minute pls')
        HTMLfile  = open('_htmlFile'+ '.html', 'w')
        HTMLfile.write('''<!--Hello-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
    <body>
                    
    </body>
</html>
        ''')
        HTMLfile.close()
        say_message('The file was created')

    elif 'create' in message and 'folder' in message:
        say_message('One minute pls')
        os.mkdir('_folder_' + str(time()) + '_' + str(randint(0,100000)))
        say_message('The folder was created')

    elif 'create' in message and 'bat' in message:
        say_message('One minute pls')
        Batfile  = open('_batFile_' + str(time()) + '.bat', 'w')
        Batfile.write('The file created')
        Batfile.close()
        say_message('The file was created')

    elif 'watch' in message and 'weather' or 'look' in message and 'weather' or 'what' in message and 'weather':
        say_message(f'Okay, i am openning sinoptik.ua')
        webbrowser.open('https://sinoptik.ua/')

    elif 'create' in message and 'py' in message or 'create' in message and 'python' in message:
        say_message('One minute pls')
        Pythonfile  = open('_pythonFile_' + str(time()) + '.py', 'w')
        Pythonfile.write('print(The file was created)')
        Pythonfile.close()
        say_message('The file was created')

    elif 'open' in message and 'telegram' in message or 'show' in message and 'telegram' in message:
        say_message('I am openning telegram')
        #your path to telegram
        os.system('"C:/Users/ktoto/AppData/Roaming/Telegram Desktop/Telegram.exe"')

    elif 'open' in message and 'calculator' in message:
        say_message('Okay, i am opening calculator')
        pyautogui.keyDown('win')
        pyautogui.press('r')
        pyautogui.keyUp('win')
        sleep(1)
        pyautogui.write('calc')
        pyautogui.press('enter')

    elif 'open' in message and 'youtube' in message or 'open' in message and 'you tube' in message:
        say_message(f'Okay, i am openning YouTube.com')
        webbrowser.open('https://www.youtube.com/')
    
    elif 'open' in message and 'google' in message:
        say_message(f'Okay, i am openning Google.com')
        webbrowser.open('https://www.google.com/')

    elif 'open' in message and 'git hub' in message or 'open' in message and 'github' in message:
        say_message(f'Okay, i am openning GitHub')
        webbrowser.open('https://github.com/')

    elif 'open' in message and 'explorer' in message:
        say_message(f'Okay, i am opening explorer')
        pyautogui.keyDown('win')
        pyautogui.press('r')
        pyautogui.keyUp('win')
        sleep(1)
        pyautogui.write('explorer.exe')
        pyautogui.press('Enter')

    elif 'open' in message and 'configuration' in message:
        say_message(f'Okay, i am opening configuration')
        pyautogui.keyDown('win')
        pyautogui.press('r')
        pyautogui.keyUp('win')
        sleep(1)
        pyautogui.write('msconfig.exe')
        pyautogui.press('Enter')

    elif 'open' in message and 'discord' in message:
        say_message('Okay, i am opening discord')
        webbrowser.open('https://discord.com/channels/@me')
#open your browser(enter your path)
    elif 'open' in message and 'browser' in message or 'open' in message and 'web browser' in message:
        say_message('Okay, i am opening browser')
        os.system('"C:\Program Files (x86)/Microsoft/Edge/Application/msedge.exe"')
#open Vs Code(enter your path)
    elif 'open' in message and 'visual studio code' in message:
        say_message('Okay, i am opening Vs Code')
        os.system('"C:/Users/ktoto/AppData/Local/Programs/Microsoft VS Code/Code.exe"')

    elif 'open' in message and 'classroom' in message or 'open' in message and 'class room' in message:
        say_message('Okay, i am opening a classroom')
        webbrowser.open('https://classroom.google.com/')
    
    elif 'open' in message and 'console' in message:
        say_message(f'Okay, i am opening console')
        pyautogui.keyDown('win')
        pyautogui.press('r')
        pyautogui.keyUp('win')
        sleep(1)
        pyautogui.write('cmd')
        pyautogui.press('Enter')
    elif "goodbye" in message:
        say_message('bye!')
        exit()


def say_message(message):
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_"+str(time())+"_"+str(randint(0,100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print("Voice assistant: "+message)
    os.remove(file_voice_name)