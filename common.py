"""
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import xml.etree.ElementTree as ET
import json
import csv
import xlwt
import pandas
"""
import pyautogui
import os
import math
import time
import numpy
import tkinter
"""
import paramiko
import sqlite3
"""

class HostSystem:
    def __init__(self, name, version, build, CPUArchTarget):
        self.name = name
        self.version = version
        self.build = build
        self.cpuArchTarget = cpuArchTarget
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getVersion(self):
        return self.version
    def setVersion(self, version):
        self.version = version
    def getBuild(self):
        return self.build
    def setBuild(self, build):
        self.build = build
    def getCPUArchTarget(self, cpuArchTarget):
        self.cpuArchTarget = cpuArchTarget

class Application:
    def __init__(self, name, path, version, build, CPUArchTarget):
        self.name = name
        self.path = path
        self.version = version
        self.build = build
        self.cpuArchTarget = cpuArchTarget
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getPath(self):
        return self.path
    def setPath(self, path):
        self.path = path
    def getVersion(self):
        return self.version
    def setVersion(self, version):
        self.version = version
    def getBuild(self):
        return self.build
    def setBuild(self, build):
        self.build = build
    def getCPUArchTarget(self, cpuArchTarget):
        self.cpuArchTarget = cpuArchTarget

class Testing:
    def __init__(self, duration, logFileName, logFileAddress):
        self.duration = duration
        self.logFileName = logFileName
        self.logFileAddress = logFileAddress
    def getDuration(self):
        return self.duration
    def setDuration(self, duration):
        self.duration = duration
    def getLogFileName(self):
        return self.logFileName
    def setLogFileName(self, logFileName):
        self.logFileName = logFileName
    def getLogFileAddress(self):
        return self.logFileAddress
    def setLogFileAddress(self, logFileAddress):
        self.logFileAddress = logFileAddress

class CLI(Testing):
    def __init__(self, name, command):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getCommand(self):
        return self.command
    def setCommand(self, command):
        self.command = command

class Window(Testing):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class TitleBar(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class MenuBar():
    def __init__(self, name='default', option='default'):
        self.name = name
        self.option = option
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getOption(self):
        return self.option
    def setOption(self, option):
        self.option = option
    def openMenu(self, name):
        if name == 'File':
            pyautogui.hotkey('alt', 'f')
            timeSleep(waitTime)
        elif name == 'View':
            pyautogui.hotkey('alt', 'v')
            timeSleep(waitTime)
        elif name == 'Report':
            pyautogui.hotkey('alt', 'r')
            timeSleep(waitTime)
        elif name == 'Favorites':
            pyautogui.hotkey('alt', 'o')
            timeSleep(waitTime)
        elif name == 'Tools':
            pyautogui.hotkey('alt', 't')
            timeSleep(waitTime)
        elif name == 'Help':
            pyautogui.hotkey('alt', 'h')
            timeSleep(waitTime)
    def openMenuOption(self, name, option):
        if name == 'File' and option == 'Preferences...':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'f')
            timeSleep(waitTime)
            for i in range(0, 0):
                pyautogui.press('down')
                timeSleep(waitTime) 
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'File' and option == 'Exit':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'f')
            timeSleep(waitTime)
            for i in range(0, 1):
                pyautogui.press('down')
                timeSleep(waitTime) 
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'View' and option == 'Toolbars':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'v')
            timeSleep(waitTime)
            for i in range(0, 0):
                pyautogui.press('down')
                timeSleep(waitTime) 
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'View' and option == 'Status Bar':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'v')
            timeSleep(waitTime)
            for i in range(0, 1):
                pyautogui.press('down')
                timeSleep(waitTime) 
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'View' and option == 'Large Icons':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'v')
            timeSleep(waitTime)
            for i in range(0, 2):
                pyautogui.press('down')
                timeSleep(waitTime) 
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'View' and option == 'Small Icons':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'v')
            timeSleep(waitTime)
            for i in range(0, 3):
                pyautogui.press('down')
                timeSleep(waitTime) 
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'View' and option == 'List':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'v')
            timeSleep(waitTime)
            for i in range(0, 4):
                pyautogui.press('down')
                timeSleep(waitTime) 
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'View' and option == 'Details':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'v')
            timeSleep(waitTime)
            for i in range(0, 5):
                pyautogui.press('down')
                timeSleep(waitTime)       
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'View' and option == 'Expand':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'v')
            timeSleep(waitTime)
            for i in range(0, 6):
                pyautogui.press('down')
                timeSleep(waitTime)         
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'View' and option == 'Collapse':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'v')
            timeSleep(waitTime)
            for i in range(0, 7):
                pyautogui.press('down')
                timeSleep(waitTime)         
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'View' and option == 'Refresh':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'v')
            timeSleep(waitTime)
            for i in range(0, 8):
                pyautogui.press('down')
                timeSleep(waitTime)        
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'Report' and option == 'Report Wizard...':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'r')
            timeSleep(waitTime)
            for i in range(0, 0):
                pyautogui.press('down')
                timeSleep(waitTime) 
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'Report' and option == 'Quick Report - All pages':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'r')
            timeSleep(waitTime)
            for i in range(0, 1):
                pyautogui.press('down')
                timeSleep(waitTime) 
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)
        elif name == 'Report' and option == 'Submit Report To FinalWire':
            pyautogui.press('esc')
            timeSleep(waitTime)
            pyautogui.hotkey('alt', 'r')
            timeSleep(waitTime)
            for i in range(0, 2):
                pyautogui.press('down')
                timeSleep(waitTime) 
            pyautogui.press('enter')
            timeSleep(waitTimeWhenOpening)

class Toolbar(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Container(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Button(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class RadioButton(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class DropDownButton(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Slider(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Label(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class TextField(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class TextBox(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class ComboBox(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class ListBox(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class CheckBox(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class MessageBox(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class DropdownList(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Toggle(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class DatePicker(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class TimePicker(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class SearchField(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Breadcrumb(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Pagination(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Tag(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Icon(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Carousel(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Notification(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class ProgressBar(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class ToolTip(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class PopUp(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Panel(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Table(Window):
    def __init__(self, name):
        self.name = name
        self.command = command
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

# Functions
def timeSleep(inputTime):
    time.sleep(inputTime)

# Variables
waitTime = 0
waitTimeWhenOpening = 1