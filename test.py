from common import *
import pyautogui
from PosReader import *

"""
testingObj = Testing(10, 'logfile.txt', 'MyAddress')
"""
pyautogui.hotkey('alt', 'tab')
timeSleep(waitTime)
menuBarObj = MenuBar()
#applicationObj = Application()
"""
print(testingObj.getDuration())
print(testingObj.getLogFileAddress())
print(testingObj.getLogFileName())
"""

"""
menuBarObj.openMenuOption('File', 'Preferences...')
menuBarObj.openMenuOption('View', 'Toolbars')
menuBarObj.openMenuOption('View', 'Status Bar')
menuBarObj.openMenuOption('View', 'Large Icons')
menuBarObj.openMenuOption('View', 'Small Icons')
menuBarObj.openMenuOption('View', 'List')
menuBarObj.openMenuOption('View', 'Details')
menuBarObj.openMenuOption('View', 'Expand')
menuBarObj.openMenuOption('View', 'Collapse')
menuBarObj.openMenuOption('View', 'Refresh')
#menuBarObj.openMenuOption('Report', 'Report Wizard...')
#menuBarObj.openMenuOption('Report', 'Quick Report - All pages')
#menuBarObj.openMenuOption('Report', 'Submit Report To FinalWire')
"""
"""
print(menuFileReadPos()['x'], menuFileReadPos()['y'])
pyautogui.click(menuFileReadPos()['x'], menuFileReadPos()['y'])
"""

#applicationObj.OpenTargetApp()
menuBarObj.mouseLeftClickMenuFile()