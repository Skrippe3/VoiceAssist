import os
import random
import speech_recognition

from function_voice import *
from function_base import *
from Music import *

with open('commands.json', 'r', encoding='utf-8') as file:
    command_dict = json.load(file)

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5



def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

        return query
    except speech_recognition.UnknownValueError:
        return 'Damn... Не понял что ты сказал :/'


def greeting():
    return 'Привет нищеброд!'

def wake_up():
    print('я')
    print("слушаю вас")
    music = Music()
    command = listen_command()
    # Регулярные выражения для команды "открой"
    open_match = re.match(r"открой\s+(.+)", command)
    video_match = re.match(r"(найди видео|запусти видео)\s+(.+)", command)
    timer_match = re.match(r"поставь таймер\s+(.+)", command)

    if open_match:
        # Захватываем часть команды после "открой"
        site_name = open_match.group(1).strip()  # Получаем всё после "открой"
        url = f"https://www.google.com/search?q={site_name}"
        webbrowser.open(url)
        return f"вот что я нашла по запросу '{site_name}'"

    elif video_match:
        # Захватываем часть команды после "найди видео" или "запусти видео"
        video_name = video_match.group(2).strip()  # Получаем всё после команды
        url = f"https://www.youtube.com/search?q={video_name}"
        webbrowser.open(url)
        return f"вот что я нашла для видео '{video_name}'"

    elif timer_match:
        # Захватываем часть команды после "поставь таймер"
        timer_text = timer_match.group(1).strip()  # Получаем всё после "поставь таймер"
        timer_seconds = w2n.word_to_num(timer_text)  # Преобразуем слова в числа
        taimer(timer_seconds)
    elif command in music.commands:
        music.execute_commands(command)
    else:
        print(random.choice(command_dict['commands']['not_understand']))
        wake_up()

def main():
    query = listen_command()

    for k, v in command_dict['commands'].items():
        if query in v:
            print(globals()[k]())


if __name__ == '__main__':
    main()