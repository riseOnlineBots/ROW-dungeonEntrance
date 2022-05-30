import sys
import threading
from time import sleep

import pyautogui as py
from pynput import keyboard

running = False
attempt = 1
is_game_buggy = False


def stop():
    global running
    running = False
    sys.exit()


# py.moveTo(1351, 1028)
#            py.click(interval=0.1)
#            py.moveTo(1392, 951)
#            py.click(interval=0.1)
#            py.moveTo(1400, 899)
#            py.click(interval=0.1)
#            py.moveTo(904, 602)
#            py.click(interval=0.1)

def run():
    global attempt, is_game_buggy

    while running:
        while True:
            py.moveTo(1800, 1373)
            py.click(interval=0.1)

            py.moveTo(1838, 1261)
            py.click(interval=0.1)

            py.moveTo(1972, 1128)
            py.click(interval=0.1)

            if is_game_buggy:
                if attempt % 2 == 0:
                    py.moveTo(1926, 1183)
                else:
                    py.moveTo(1922, 1209)

            py.click(interval=0.1)
            py.moveTo(1858, 1188)
            py.click(interval=0.6)
            py.moveTo(1224, 796)
            py.click(interval=0.1)

            attempt += 1

            if is_game_buggy:
                sleep(2)


def process():
    run()


def on_press(key):
    global running, attempt

    if key == keyboard.Key.esc:
        print('The bot ran for %s time(s).'.format(attempt))
        stop()

        return False  # Stops the listener.
    try:
        k = key.char  # Single-char keys.
    except:
        k = key.name
    if k in ['f12']:
        running = True
        threading.Thread(target=process).start()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# pyinstaller --onefile C:\Users\undefined\PycharmProjects\pythonProject\main.py --paths C:\Users\undefined\PycharmProjects\pythonProject\venv\Lib\site-packages
