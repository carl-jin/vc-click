import keyboard  # using module keyboard
import time
import pyautogui

# 打包 pyinstaller -F main.py -n vc-click

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('caps lock'):  # if key 'q' is pressed 
            pos = pyautogui.position()
            print('Trigger click, mouse position',pos.x,pos.y)
            pyautogui.click(x=pos.x, y=pos.y)
            time.sleep(0.1)
         
    except:
        break