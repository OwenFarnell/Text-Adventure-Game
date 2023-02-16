import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    time.sleep(2)
    print("You wake up in a room with no windows and only one door.")
    time.sleep(2)
    print("Your objective is to escape this room.")
    time.sleep(2)

def room():
    print("You are in a room with a bed, a desk, and a closet.")
    time.sleep(2)
    print("What do you want to do?")
    time.sleep(1)
    choice = input("1. Check the bed\n2. Check the desk\n3. Check the closet\n")
    if choice == "1":
        print("You find nothing interesting on the bed.")
    elif choice == "2":
        print("You find a key in one of the drawers.")
    elif choice == "3":
        print("You find a note that reads 'The key is under the bed.'")
    else:
        print("Invalid input.")
        room()

def escape():
    print("You have the key. You use it to unlock the door.")
    time.sleep(2)
    print("You have successfully escaped the room!")
    time.sleep(2)

introduction()
room()

while True:
    if "key" in globals():
        escape()
        break
    else:
        print("What do you want to do?")
        time.sleep(1)
        choice = input("1. Check the bed\n2. Check the desk\n3. Check the closet\n")
        if choice == "1":
            print("You find nothing interesting on the bed.")
        elif choice == "2":
            print("You find a key in one of the drawers.")
            global key
            key = True
        elif choice == "3":
            print("You find a note that reads 'The key is under the bed.'")
        else:
            print("Invalid input.")
