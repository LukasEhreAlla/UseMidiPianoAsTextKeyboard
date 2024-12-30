
import Main

def note_to_string(note):
    """Convert MIDI note number to string representation (e.g., E3)."""
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = (note // 12)
    note_name = note_names[note % 12]
    return f"{note_name}{octave}"

def isBlack(num):
    noteNum= (num % 12)
    
    #print("Is black aufgerufen", noteNum)
    if(noteNum==1 or noteNum==3 or noteNum==6 or noteNum==8 or noteNum==10):
        return True
    else:
        return False
    
class Note:
    num = None
    name = None
    button = None
    
    def __init__(self,number) -> None:
        #print(self)
        self.num = number
        self.name = note_to_string(number)
        self.button = None
        
        
     
    
    def getNum(self):
        return self.num

    def getName(self):
        return self.name
    
    def getButton(self):
        return self.button
    
    def toDictionary(self):
        thisdict = {
                "name": self.name,
                "num": self.num,
                 "button": self.button
                    }
        return thisdict
    def setButton(self,button):
        self.button=button
    
    
if __name__ == "__main__":
    Main.main()