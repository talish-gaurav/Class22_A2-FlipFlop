def palind(r):
    e = len(r) - 1
    s = 0
    while(s<e):
        if r[s]!=r[e]:
            return False
        s+=1
        e-=1
    return(True)

r = ("r","a","c","e","c","a","r")

if(palind(r)):
    print("A flip - flop")
else:
    print("Not a flip-flop")