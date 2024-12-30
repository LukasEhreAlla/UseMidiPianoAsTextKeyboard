import Note
import Main
actives = []

def getActives():
    return actives

def addActives(note):
    
    actives.append(note)
    #print (toString())

    
def deleteActive(note):
    try:
        actives.remove(note)
   #print (toString())
    except:
        #print("tryed Removing Note, error, probably not there")
        pass
def returnSpecificNote(num)-> Note:
    for x in actives: 
        if (x.getNum()==num):
            
            return x

def toString():
    
    n="\n"
    for x in actives:
        n= n + x.getName()
        n= n + ","
    n = n[:-1]    
    n= n +"\n"
    
    return n


if __name__ == "__main__":
    Main.main()