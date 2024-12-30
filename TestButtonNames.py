import keyboard
print("Press a Key on your Keyboard to see its Name")
def test(callback):
    
    print(callback.name)

keyboard.on_press(test)
keyboard.wait() 