import Main
import webbrowser


history = []
def log(n):
    
    history.append(n)
    while(len(history)>8):
        for x in range (len(history)-1):
            history[x]=history[x+1] 
        history.pop() 
        
    if (history==[67, 66, 63, 57, 56, 64, 68, 72]) or history ==[79,78,75,69,68,76,80,84]:
        easteregg()
    #print(history)
    
def easteregg():
    print("easteregg")  
    webbrowser.open('https://r.mtdv.me/-QYjeF0fLp') 
    
    
if __name__ == "__main__":
    Main.main()