from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller

mouse = Controller()
time.sleep(10)
counter = 0

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

window_name = input('\n[✅] | Введите название нужного вам окна или (1 - TelegramDesktop): ')

if window_name == '1':
    window_name = "TelegramDesktop"

check = gw.getWindowsWithTitle(window_name)
if not check:
    print(f"[❌] | Окно - {window_name} не найдено!")
else:
    print(f"[✅] | Окно найдено - {window_name}\n[✅] | Нажмите 'q' для паузы.")

telegram_window = check[0]
paused = False

while True:
    if keyboard.is_pressed('q'):
        paused = not paused
        if paused:
            print('[✅] | Пауза.')
        else:
            print('[✅] | Продолжение работы.')
        time.sleep(0.2)

    if paused:
        continue

    window_rect = (
        telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
    )

    if telegram_window != []:
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

    scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

    width, height = scrn.size
    pixel_found = False
    if pixel_found == True:
        break
        
    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = scrn.getpixel((x, y))
            if ((b in range(200, 255)) and (r in range(0, 100)) and (g in range(150, 255))) or \
                    ((b in range(0, 135)) and (r in range(112, 220)) and (g in range(210, 255))):
                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y
                click(screen_x + 4, screen_y)
                time.sleep(0.0421 + random.uniform(0.001,0.01))
                pixel_found = True
                break
            r, g, b = scrn.getpixel((50, 757))
            if  r == 255 and g == 255 and b == 255: 
                click(window_rect[0] + 50, window_rect[1]+757)




print('[✅] | Остановлено.')
