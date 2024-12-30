import keyboard 
import Main
def pressKey(keyName):
    try:
        keyboard.press(keyName)
    except:
        #print("no key bound")
        pass
    
    
    
def releaseKey(keyName):
    try:
        keyboard.release(keyName)
    except:
        pass
    
    
if __name__ == "__main__":
    Main.main()
    
    
    
