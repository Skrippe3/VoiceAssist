from main import *
from moduls import *

def create_task():
    print('Что добавим в список дел?')
    query = listen_command()

    with open('todo-list.txt', 'a') as file:
        file.write(f'{query}\n')
    return f'Задача {query} добавлена в список дел'

def open_google():
    os.startfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    print("Хорошо")

def bye_Eva():
    print('Досвидание')
    quit()


def open_task():
    file = open("todo-list.txt", "r")
    content = file.read()
    print(content)
    file.close()


def off_pc():
    os.system('shutdown /s /t 1')


def pause_pleer():
    pyautogui.press('space')
    return 0

def weather():
    owm = OWM('9cf535e1afad6ef848ea7b5491931ac2')
    manager = owm.weather_manager()
    place = manager.weather_at_place('Rostov, RU')
    res = place.weather
    value = int(res.temperature('celsius')['temp'])
    print(f'В Ростове {value}')

def sany_pid():
    print('эх саня я как и ты был на цепи хлебал хозяйские харчи')


