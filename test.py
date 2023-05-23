import speech_recognition as sr
from gtts import gTTS
import random
import playsound
import os

def listen():           #слушает что я говорю в микро
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Слушаю команду")
        audio = voice_recognizer.listen(source)

    try:
        voice_text = voice_recognizer.recognize_google(audio, language='ru').lower()
        print(f"вы сказали {voice_text}")
        return voice_text
    except sr.UnknownValueError:
        return 'ошибка распознования'
    except sr.RequestError:
        return 'ошибка запроса'

def say(text):              # воспроизведение
    voice = gTTS(text, lang='ru')
    unique_file = 'audio_' + str(random.randint(0, 10000)) + '.mp3'
    voice.save(unique_file)
    playsound.playsound(unique_file)
    os.remove(unique_file)

    print(f'Ассистент: {text}')


def handle_command(command):
    command = command.lower()

    if command == "привет":
        say('приветулики')
    elif command == 'пока':
        stop()
    else:
        say('Не понятна начальника')



def stop():
    say('До скорого')
    exit()


def start():
    print('запуск ассистента...')

    while True:
        command = listen()
        def handle_command(command):

try:
    start()
except KeyboardInterrupt:
    stop()