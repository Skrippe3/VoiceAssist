from moduls import *
from main import *


class Music:
    def __init__(self, url='https://music.yandex.ru/home'):
        self.url = url

        self.commands = {
            "включи музыку": self.play_music,
            "дальше": self.next_music,
            "назад": self.back_music,
            "лайк": self.like_music,
            "громче": lambda: pyautogui.press('+'),
            "тише": lambda: pyautogui.press('-')
        }

    def play_music(self):  # в будущем реализовать парсинг страницы
        webbrowser.open(self.url)
        time.sleep(5)
        pyautogui.press("space")

    def next_music(self):
        pyautogui.press('l')

    def back_music(self):
        pyautogui.press('k')

    def like_music(self):
        pyautogui.press('f')

    def execute_commands(self, command_key):
        if command_key in self.commands:
            self.commands[command_key]()

