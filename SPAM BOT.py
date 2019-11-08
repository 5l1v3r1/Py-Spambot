import pyautogui
spam = input("What do you want to spam? : ")
while True:
    pyautogui.typewrite('%s' % spam)
    pyautogui.press('enter')
