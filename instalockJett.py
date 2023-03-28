import pyautogui
import time
import keyboard
print("Starting in 5 seconds...")
print(pyautogui.size())
print(pyautogui.position())


razeCordsX = 775
razeCordsY = 984
reynaCordsX = 883
reynaCordsY = 997
jettCordsX = 1050
jettCordsY = 929


while keyboard.is_pressed('e') == False:
    time.sleep(0.1)
    print("Waiting for F to be pressed")
    if keyboard.is_pressed('f'):
        print("F was pressed")
        for i in range(0,51):
            pyautogui.click(jettCordsX,jettCordsY)
            pyautogui.click(1002,820)
            clicked = i+1
            print("Clicked " + str(clicked) + " times")
            time.sleep(0.1)
            if keyboard.is_pressed('e'):
                print("E was pressed, exiting script")
                break
