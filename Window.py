import tkinter as tk
import Main
from tkinter import filedialog
from functools import partial
import Note
import keyboard 
import time
import json

allPianoButtons=[]
blackButtons=[]

c=1

def startWindow():
    

    
    
    global root
    """
        # Wait until alreadyCreatedNotes is populated
    while not Main.alreadyCreatedNotes:
        time.sleep(0.1)  # Avoid busy-waiting; adjust if necessary
    """
    

    nameTextForKey=""
    root = tk.Tk()
    root.title("Midi to ComputerKeyboard")
    root.geometry("1080x500")
    previousBlacksNumber=0
    
    for i in range (21):
        allPianoButtons.append( tk.Button(root, text=(str(i)+"\n"+nameTextForKey),  command= partial(buttonPress,(i))))
        allPianoButtons[i].place(x= 10+i*40, y=300, width=40 , height=40)
    
    for i in range (88):
        try:
            for note in Main.alreadyCreatedNotes:
                if note.getNum()==(i+21):
                    nameTextForKey=str(note.getButton())
                    
                    if(nameTextForKey=="none" or nameTextForKey=="None"):
                        nameTextForKey=""
        except:
            print("Error labeling piano keys")
        print(i+21, nameTextForKey)
        allPianoButtons.append( tk.Button(root, text=(f"{Note.note_to_string(i+21)} \n {nameTextForKey}"),  command= partial(buttonPress,(i+21))))
        
        
        
        if(Note.isBlack(i+21)):
            
            allPianoButtons[i+21].config(bg="black", fg="green")
            
            allPianoButtons[i+21].place(x= 10+i*20-(previousBlacksNumber*20) , y=375, width=18 , height=70)
            blackButtons.append(allPianoButtons[i+21])
            previousBlacksNumber=previousBlacksNumber+1
        else:
           allPianoButtons[i+21].place(x= 20+i*20-(previousBlacksNumber*20) , y=375, width=20 , height=100) 
           allPianoButtons[i+21].config(text= f"\n \n \n \n \n {Note.note_to_string(i+21)} \n {nameTextForKey}") 
    
    
    for i in blackButtons:
        i.tkraise()
    
    resizeButton=tk.Button(root, text="Resize Piano",  command=resizeButtons)     
    resizeButton.pack(side="left",anchor="nw") 
    
    onOffSwitch=tk.Button(root, text="Switch off, currently on", command=toggleActive, background="green2")
    onOffSwitch.pack(side="right",anchor="ne", pady=20,padx=20) 
    """
    exportButton=tk.Button(root, text="Export settings to file", command=exportSettings) 
    exportButton.pack(side="left",anchor="nw") 
    
    importButton=tk.Button(root, text="Import settings from file", command=importSettings) 
    importButton.pack(side="left",anchor="nw") 
    

    
    deviceButton=tk.Button(root, text="Switch MIDI Input Device", )
    deviceButton.pack(side="left",anchor="nw")
    """
    
    root.mainloop()
    
    
def buttonPress(num):
    #wird aufgerufen, wenn in GUI Taste geklickt wird
    """assignKeyWindow(num)"""

def resizeButtons():

    for i in range (21):
        
        allPianoButtons[i].place(x= 10+i*40, y=300, width=40 , height=40)
    
    c=root.winfo_width()/1080
    windowHeight = root.winfo_height()
    previousBlacksNumber=0
    
    for i in range (88):
        allPianoButtons[i+21].config(font=("TkDefaulFont",int(windowHeight/65)))
        if(Note.isBlack(i+21)):
            
                
            
             allPianoButtons[i+21].place(x= c*(10+i*20-(previousBlacksNumber*20)) , y=windowHeight-c*125, width=c*18 , height=c*70)
            
             previousBlacksNumber=previousBlacksNumber+1
        else:
              allPianoButtons[i+21].place(x= c*(20+i*20-(previousBlacksNumber*20)) , y=windowHeight-c*125, width=c*20 , height=c*100)
    
    for i in blackButtons:
        i.tkraise()       
        
    for i in range (21):
        
        allPianoButtons[i].place(x= c*(10+i*40), y=windowHeight-c*200, width=c*40 , height=c*40)
    
    


def makeButtonRed(NoteNum):
    allPianoButtons[NoteNum].config(bg="red")
def makeButtonNormal(NoteNum):
    if allPianoButtons[NoteNum] in blackButtons:
        allPianoButtons[NoteNum].config(bg="black")
    else:
        allPianoButtons[NoteNum].config(bg="white")
    
"""
def assignKeyWindow(num):
    
    root2=tk.Tk()
    root2.title(f"Assign Keyboard Key to Midi  {num} ({Note.note_to_string(num)})")
    root2.geometry("600x600")
    
    root2.afterID = None
    
    KeyBindingDisplay = tk.Label(root2, text=f"Assign a computer key to MIDI note {num} ({Note.note_to_string(num)}) \n by pressing it on your computer keyboard", width=400,font=("TkDefaulFont",20))
    KeyBindingDisplay.pack(pady=200)
    
    hook_id=keyboard.hook(partial(comKeyPressed,KeyBindingDisplay,num))
    saveButton=tk.Button(root2, text="Save",command = partial(saveKeybind,num,hook_id,KeyBindingDisplay,root2), width=20, height=3,background="grey75")
     
    noneButton=tk.Button(root2, text="Set empty keybind (standard)",command = partial(noneButtonPressed,KeyBindingDisplay,num), width=30, height=3,background="grey75")
    saveButton.pack(side="right",anchor="s")
    
    noneButton.pack(side="right",anchor="s")
    
    
    
  
    root2.mainloop()
    
def comKeyPressed(KeyBindingDisplay,num,comKey):
    
    #comKey as in Computer Key as in not a Piano Keyboard
    if (comKey.event_type=="down"):
        #print(comKey.name)
        global currentComKey
        currentComKey=comKey
        
        KeyBindingDisplay.configure(text=f"Currently binding {comKey.name} to the {num} {Note.note_to_string(num)} MIDI key")

def noneButtonPressed(KeyBindingDisplay,num):        
    global currentComKey
    currentComKey = None
    KeyBindingDisplay.configure(text=f"Currently binding Empty/Nothing \n to the {num} {Note.note_to_string(num)} MIDI key")
        
def saveKeybind(num,hook_id,KeyBindingDisplay,root2):
    
       
        note=Main.getNoteByNum(num)
        try:
            if currentComKey != None:
                note.setButton(str(currentComKey.name))
            else:
                note.setButton(None)


            KeyBindingDisplay.configure(text="SAVED", background="grey75")
            
        except NameError:
            KeyBindingDisplay.configure(text="Error, set nothing before \n saving, saving empty", background="red")
            note.setButton(None)
            
        alreadyPressedSaveButton=False
        for widget in root2.winfo_children():
            
            if isinstance(widget, tk.Button) and widget.cget("text") == "Close":
                alreadyPressedSaveButton=True
                
            
            if isinstance(widget, tk.Button) and widget.cget("text") == "Save":
                saveButton=widget
                saveButton.config(text="Close")

                
            if isinstance(widget, tk.Button) and widget.cget("text") == "Set empty keybind (standard)":
                noneButton = widget
                noneButton.destroy()
        if not alreadyPressedSaveButton:
            Main.saveToJson()   
            Main.readFromJson()
            keyboard.unhook(hook_id) 
        #get nine button here
        
            root2.afterID=root2.after(2000, root2.destroy)
        else:
            root2.after_cancel(root2.afterID)
            root2.destroy()
"""        
    
        
""" 
def exportSettings():
    path = filedialog.asksaveasfilename(filetypes=[("json file", ".json")])
    
    Main.saveToJsonByName(f"{path}.json")     

def importSettings():
    path = filedialog.askopenfilename(filetypes=[("json file", ".json")])
    
    Main.alreadyCreatedNotes.clear()
    for x in Main.readFromJsonByName(path):
        Main.alreadyCreatedNotes.append(x)
        Main.saveToJson()
"""    

def toggleActive():
    for widget in root.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget("text") == "Switch on, currently off" or widget.cget("text") == "Switch off, currently on":
                onOffSwitch= widget
    
    if Main.useProgram:
        onOffSwitch.config(background="red",text="Switch on, currently off")
        Main.useProgram = False
        
    else:
        onOffSwitch.config(background="green2",text="Switch off, currently on")
        Main.useProgram= True
        


if __name__ == "__main__":
    Main.main()
    
