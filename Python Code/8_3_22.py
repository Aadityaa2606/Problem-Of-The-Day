S = input('').split(' ')

def wrd_returner(l):
    Cinit =[]
    for wrd in S:
        if wrd.find(l) != -1:
            Cinit.append(wrd)
    return Cinit  

def vowel_checker(word):
    vows="AEIOUaeiou"
    cntr=0
    for i in word:
        if i in vows:
            cntr +=1
    return cntr

def Flogic(wrd):
    for i in wrd:
        Thewrds = wrd_returner(i)
        if len(Thewrds) != 2:
            return False
        if vowel_checker(Thewrds[0]) != vowel_checker(Thewrds[1]):
                return False
    return True

for wrd in S:
    if Flogic(wrd):
        print(wrd)
