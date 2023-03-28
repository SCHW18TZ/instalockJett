import pyautogui
import time

print("Starting in 5 seconds...")
print(pyautogui.size())
print(pyautogui.position())

jettCords = (1090,929)
reynaCords = (883,997)
razeCordsX = 775
razeCordsY = 984

def intsalockJett():
    for i in range(0,51):
        pyautogui.click(1090,929)
        pyautogui.click(1002,820)
        clicked = i+1
        print("Clicked " + str(clicked) + " times")   

def instalockReyna():
    for i in range(0,51):
        pyautogui.click(883,997)
        pyautogui.click(1002,820)
        clicked = i+1
        print("Clicked " + str(clicked) + " times")

def instalockRaze():
    for i in range(0,51):
        pyautogui.click(775,984)
        pyautogui.click(1002,820)
        clicked = i+1
        print("Clicked " + str(clicked) + " times")


def instalockAnything (x,y):
    for i in range(0,51):
        pyautogui.click(x,y)
        pyautogui.click(1002,820)
        clicked = i+1
        print("Clicked " + str(clicked) + " times")

instalockAnything(razeCordsX,razeCordsY) 