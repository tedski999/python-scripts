from pynput import keyboard
import time

isRunning = True
currentNumber = 616

def on_press(key):
	if key == keyboard.Key.esc:
		global isRunning
		isRunning = False
		print("Quitting...")

def press_key(key):
	keyboardController.press(key)
	time.sleep(0.1)
	keyboardController.release(key)

keyboardController = keyboard.Controller()
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Starting in 5 seconds...")
time.sleep(5)

while isRunning:
	characters = str(currentNumber)
	for char in characters:
		time.sleep(0.25)
		press_key(char)
	time.sleep(1.5)
	if not isRunning:
		break
	press_key(keyboard.Key.enter)
	currentNumber += 1
	time.sleep(5)
