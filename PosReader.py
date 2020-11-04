import pyautogui

def menuFileReadPos():
    posx, posy = pyautogui.locateCenterOnScreen('Resources/Screenshots/MenuFile.PNG')
    return {
        'x': posx,
        'y': posy
    }

def titleBarMainWindowReadPos():
    posx, posy = pyautogui.locateCenterOnScreen('Resources/Screenshots/TitleBarMainWindow.PNG')
    return {
        'x': posx,
        'y': posy
    }