import pyautogui
import pyperclip
import time


def type_letter(letter):

    pyautogui.write(letter)

def new_tab(input):
    pyautogui.press("win")
    pyautogui.write("google chrome")
    time.sleep(0.5)
    pyautogui.press("right")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1.5)

    pyautogui.write("http://chatgpt.com")
    pyautogui.press("enter")
    time.sleep(1.5)

    pyautogui.write(input)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(8)

    clickLowest("images\copy_button.PNG")

    time.sleep(0.5)

    return pyperclip.paste()

def clickLowest(image):
    matches = list(pyautogui.locateAllOnScreen(
        image,
        confidence=0.9
    ))

    if not matches:
        return "Images not found"

    lowest = max(matches, key=lambda box: box.top)

    pyautogui.click(pyautogui.center(lowest))

    return "Clicked lowest"