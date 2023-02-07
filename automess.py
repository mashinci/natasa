import pyautogui
import time


message_content = "Automatska poruka na 5 sekundi"

time.sleep(10)

while True:
    pyautogui.write(message_content)
    pyautogui.press('enter')
    time.sleep(5)