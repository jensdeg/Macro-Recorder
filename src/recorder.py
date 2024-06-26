import pyautogui
import win32api
import time

Recording = []


def Start():
    print("Recording started...")
    
    while True:
        # x,y are location. T is time it was clicked         
        X,Y,T = GetClick(time.perf_counter())

        # adds click to recording
        click = (X,Y),T
        Recording.append(click)

        print(Recording)



# Gets the entire click event including position and time
def GetClick(Starting_Time):
    X,Y = getPosition()
    T = GetTime(Starting_Time)
    return X,Y,T


# Gets the time in seconds after the recording has started
def GetTime(Starttime):
    return time.perf_counter() - Starttime

# gets current mouse position
def getPosition():
    # from https://stackoverflow.com/questions/165495/detecting-mouse-clicks-in-windows-using-pythonimport pyautogui
    state_left = win32api.GetKeyState(0x02)  # right button down = 0 or 1. Button up = -127 or -128

    
    while True:
        a = win32api.GetKeyState(0x01)
        if a != state_left:  # Button state changed
            state_left = a
            if a < 0:  # Button pressed down
                x, y = pyautogui.position()
                while win32api.GetKeyState(0x01) < 0:  # Wait for button release
                    time.sleep(0.001)
                return x, y
        time.sleep(0.001)