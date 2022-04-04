
matchups = {
 'R': 'S',
 'P': 'R',
 'S': 'P'
}


def Jokenpo(p1: str, p2: str):
    
    if p1 == p2:
        return 'Tie'
    
    if matchups[p1] == p2:
        return p1
    else:
        return p2
    
    
