import pyautogui
from time import sleep
# sleep(5)
# for i in range(0,3):
#     pyautogui.write('I love you, Python', interval=0.25)
#     pyautogui.press('enter')

while True:
    pyautogui.typewrite("#")
    sleep(2)
    pyautogui.press("enter")