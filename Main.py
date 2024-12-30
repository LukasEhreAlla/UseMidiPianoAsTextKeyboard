import mido
import ActiveNotes
import ZeldaEasteregg
import Note
import Outputkeys
import json
import tkinter as tk
import threading
import Window
import os
import Main

alreadyCreatedNotes =[]  
global useProgram
useProgram = bool(True)

def main():
    
    for x in readFromJson():
        #print(x.getName())
        alreadyCreatedNotes.append(x)
    
    t1 = threading.Thread(target=midiShit, args=())
    t1.daemon = True
    t1.start()
    Window.startWindow()
    
    
    
    
    
    
def midiShit():    
    #midi setup:
    print(mido.get_input_names())
    input_name = mido.get_input_names()[0]
    


    
    #print(alreadyCreatedNotes)
    
    with mido.open_input(input_name) as inport:
        print(f"Listening for MIDI input on {input_name}...")
        
        for msg in inport:
            if msg.type == 'note_on' and msg.velocity > 0 and useProgram:
                
                #print (useProgram)
                matches=False
                for x in alreadyCreatedNotes:
                    if(x.getNum()==msg.note):
                        note=x
                        matches=True
                if(matches==False):
                    note = Note.Note(msg.note)
                    alreadyCreatedNotes.append(note)
                    #saveToJson()
                

                ZeldaEasteregg.log(note.getNum())
                print(note.getName(),note.getNum(), " - Button:", note.getButton())
                #print(msg.note)
                
                ActiveNotes.addActives(note)
                Window.makeButtonRed(msg.note)
                Outputkeys.pressKey(note.getButton())
                
            if msg.type == 'note_off' and msg.velocity > 0:
                
                matches=False
                for x in alreadyCreatedNotes:
                    if(x.getNum()==msg.note):
                        note=x
                        matches=True
                if(matches==False):
                    note = Note.Note(msg.note)
                    alreadyCreatedNotes.append(note)
                    #saveToJson()
                
                #print(note.getName(), "off")
                Outputkeys.releaseKey(note.getButton())
                Window.makeButtonNormal(msg.note)
                ActiveNotes.deleteActive(note)
"""                
def saveToJson():
    dictionary={}
    i=0
    for x in alreadyCreatedNotes:
        dictionary[(i)]=x.toDictionary()
        i=i+1
    #print (dictionary)    
    with open('CurrentSettings.json', 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)
"""
def readFromJson():
    array=[]
    #print(f"Current working directory: {os.getcwd()}")
    try:
        
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'Keybinds.json')
    
        with open(file_path) as f:
            d = json.load(f)
        
            for i in range (len(d)):
            
                newNote= Note.Note(d[str(i)]["num"])
                newNote.setButton(d[str(i)]["button"])
                array.append(newNote)
    except:
        print("Error with reading keybinds.json")
    return array             
"""
def saveToJsonByName(path):
    dictionary = {}
    for i, x in enumerate(alreadyCreatedNotes):
        dictionary[i] = x.toDictionary()

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)
def readFromJsonByName(path):
    array=[]
    try:
    if True:
        with open(path) as f:
            d = json.load(f)
        
            for i in range (len(d)):
            
                newNote= Note.Note(d[str(i)]["num"])
                newNote.setButton(d[str(i)]["button"])
                array.append(newNote)
    except:
        print("Error, json probably empty")
    return array             
"""     
def getNoteByNum(num):
    for x in alreadyCreatedNotes:
        if x.getNum() == num:
            return x
    note = Note.Note(num)
    alreadyCreatedNotes.append(note)
    #saveToJson()
    return note
            
    
    
 
 
 
 
    

if __name__ == "__main__":
    Main.main()