import pyautogui
import time

print("Starting in 5 seconds...")
print(pyautogui.size())
print(pyautogui.position())

def intsalockJett():
    for i in range(0,51):
        pyautogui.click(1090,929)
        pyautogui.click(1002,820)
        clicked = i+1
        print("Clicked " + str(clicked) + " times")   

intsalockJett()