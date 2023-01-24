import pyautogui ,time
time.sleep(5)

with open("testing.txt", "r") as tulisan:
    for text in tulisan:
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        time.sleep(1)







