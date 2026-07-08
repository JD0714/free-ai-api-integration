import pyautogui
import time


def type_letter(letter):

    pyautogui.write(letter)

def newTab(input):
    time.sleep(3)
    pyautogui.press("win")
    pyautogui.write("google chrome")
    time.sleep(1)

    pyautogui.press("up")
    time.sleep(1)
    pyautogui.press("right")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.press("right")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    pyautogui.write("http://chatgpt.com")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.write(input)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)