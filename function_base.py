from moduls import *

def calculate():
    return None

def taimer(timer):
    time_sec = timer * 60
    for tik in range(time_sec):
        time.sleep(1)
        time_sec -= 1
        if time_sec == 0:
            print('Таймер завершен')