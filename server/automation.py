import pyautogui
import pyperclip
import time

def doStart(input):
    pyautogui.press("win")
    time.sleep(0.5)
    pyautogui.write("chrome")
    time.sleep(1)
    pyautogui.press("right")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1.5)

    pyautogui.write("http://chatgpt.com")
    pyautogui.press("enter")
    time.sleep(3)

    pyautogui.write(input)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(10)

    clickLowest(r"images\copy_button.png")

    time.sleep(0.5)

    return pyperclip.paste()

def doContinue(input):
    pyautogui.write(input)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(10)

    clickLowest(r"images\copy_button.png")

    time.sleep(0.5)

    return pyperclip.paste()

def doEnd():
    pyautogui.hotkey('ctrl', 'w')
    return "Command executed"

def clickLowest(image):
    matches = list(pyautogui.locateAllOnScreen(
        image,
        confidence=0.5
    ))

    if not matches:
        return "Images not found"

    lowest = max(matches, key=lambda box: box.top)

    pyautogui.click(pyautogui.center(lowest))

    return "Clicked lowest"