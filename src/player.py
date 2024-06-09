import pyautogui
import time

TestRecording = [((1208, 209), 0.3802398000007088),
                ((949, 413), 0.9315409999999247),
                ((1414, 404), 1.6026411000002554)]


for click in TestRecording:
    time.sleep(click[1])
    pyautogui.click(click[0])

