import ctypes
import time
import datetime
from datetime import datetime
import locale
import speech_recognition
from gtts import gTTS
import random
import subprocess
import playsound
import os
import pyautogui
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
import pycaw
from pycaw.pycaw import (AudioUtilities,IAudioEndpointVolume,ISimpleAudioVolume)

import list_text  # тут списки текстов для шуток , предсказаний и анеклотов
import commands

sr = speech_recognition.Recognizer()
sr.pause_threshold=0.5





def shutki():
    abs = random.randrange(len(list_text.list_shutok))  # текст со списком слов+рандом на его*   ++++++++++
    sss = list_text.list_shutok[abs]
    say(sss)




def anekdot():
    a = random.randrange(len(list_text.list_anekdot))  # текст со списком слов+рандом на его*   ++++++++++ изменить на шадание
    aa = list_text.list_anekdot[a]
    say(aa)




def predskazanya():
    a = random.randrange(len(list_text.prediction_text))             #текст со списком слов+рандом на его*   ++++++++++ изменить на шадание
    aa=list_text.prediction_text[a]
    say(aa)



def listen_command():
    #tфункция вернет распознанную команду
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.2)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-Ru').lower()
            print(f"ты сказал {query}")
            return query
    except speech_recognition.UnknownValueError:
        return "Damn... не понял что ты сказал"



def what_time():
    now = datetime.datetime.now()
    say(f"Текущее время:, {now.time().strftime('%H:%M:%S')}")



def what_date():
    locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
    nowe = datetime.now()
    a = nowe.strftime('сегодня %A, %d-го %B %Y-го  ',)
    say(a)



def open_spotyfy():
    os.startfile(r'"C:\Users\Pi1ners\AppData\Roaming\Spotify\Spotify.exe"')


def play():
    return pyautogui.press('playpause')  # пауза / play


def nexttrack():
    return pyautogui.press('nexttrack')  # следующий трек


def prevtrack():
    return pyautogui.press('prevtrack')  # прошлый трек


def volumup():
    return pyautogui.press('volumeup')  # звук громче


def volumdown():
    return pyautogui.press('volumedown')  # звук тише



def volume_on():                #включение звука на громкость которая была перед его выключением
    say('выполнено')
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(0, None)


def volume_off():               # громкость на 0.....если вернуть будет
    say("готово")
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(1, None)


def volume_na():
    say('выстовляю')
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(pycaw.pycaw.IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(pycaw.pycaw.IAudioEndpointVolume)

    # Устанавливаем громкость на 50%
    volume.SetMasterVolumeLevel(-50.0, None)


def say(text):              # воспроизведение голоса
    voice = gTTS(text, lang='ru')
    unique_file = 'audio_' + str(random.randint(0, 10000)) + '.mp3'
    voice.save(unique_file)
    playsound.playsound(unique_file)
    os.remove(unique_file)

    print(f'Ассистент: {text}')


def greeting():
    #приветствие
    return say("привет нищеброд")


def create_task():
    #добавление заметок
    say("что добавим в список дел?")

    query = listen_command()

    with open('todo-list.txt', 'a') as file:
        file.write(f"{query}\n")
    return say(f'задача {query} добавлени в список todo-list')



def delete_task():   ###################   ПРОРАБОАТЬ
    say("что будем удалять?")
    query = listen_command()

    with open('todo-list.txt', 'r+') as file:
        lines = file.readlines()
        print(lines)
        if query == lines:
            lines.remove(f'{query}\n')
        else:
            return say(f'задачи {query} в файле не найдено')


def main():
    while True:
        query = listen_command()

        for k, v in  commands.commands_dict['commands'].items():
            if query in v:
                print(globals()[k]())


def stop():
    say('до скорого')
    exit()




if __name__ in "__main__":
    main()



