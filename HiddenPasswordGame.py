import os
import random
import threading

loop = 1
hintSize = len(os.getcwd())+1
startHintSize = hintSize-1
passcode = random.randrange(999999999)

print("Starting at: " + os.getcwd())

while loop == 1:
    files = os.listdir()
    dirs = [f for f in files if os.path.isdir(f)]
    if random.randrange(5) == 1:
        loop = 0
    else:
        if len(dirs) == 0:
            loop = 0
        else:
            randomdir = random.sample(dirs,1)
            os.chdir(randomdir[0])

hint = str(os.getcwd())
file=open("passcode.txt","w")
file.write(str(passcode))
file.close()

while 1>0:
    if input("Passcode: ") == str(passcode):
        print("You won in " + str(hintSize-startHintSize) + " guess!\n\nDeleting file...")
        break
    else:
        hintSize += 1
        print("Wrong...\nHint: " + hint[0:hintSize])

try:
    os.remove("passcode.txt")
    print("Deleted.")
except FileNotFoundError:
    print("File already deleted.")

input("\nPress Enter to exit...")
