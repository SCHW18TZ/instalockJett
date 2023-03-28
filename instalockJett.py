import pyautogui
import time
import keyboard
print("Starting in 5 seconds...")
print(pyautogui.size())
print(pyautogui.position())


razeCordsX =629
razeCordsY = 1025
reynaCordsX = 714
reynaCordsY = 1025
jettCordsX = 1022
jettCordsY = 930


while keyboard.is_pressed('e') == False:
    time.sleep(0.1)
    print("Waiting for F to be pressed")
    if keyboard.is_pressed('f'):
        print("F was pressed")
        for i in range(0,51):
            pyautogui.click(reynaCordsX,reynaCordsY)
            pyautogui.click(1002,820)
            clicked = i+1
            print("Clicked " + str(clicked) + " times")
            time.sleep(0.1)
            if keyboard.is_pressed('e'):
                print("E was pressed, exiting script")
                break
