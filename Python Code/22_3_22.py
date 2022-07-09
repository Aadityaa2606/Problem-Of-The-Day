n = int(input(''))

def stringformer(n):
    S = ''
    while n!=0:
        r = n%3
        q = n//3
        n = q
        if r == 0:
            S+='r'
        elif r == 1:
            S+='g'
        else:
            S+='b'
    S+='r'*(20-len(S))
    return S[::-1]

def compare(s1,s2):
    chk=0
    for i in range(20):
        if s1[i] != s2[i]:
            chk+=1
    return chk

Fs = stringformer(n)
x=True
y=True
cntr1=n+1
cntr2=n+1
S2=''
S3=''
while x:
    st1 = stringformer(cntr1)
    if compare(Fs, st1) == 1:
        S2=st1
        x = False
    cntr1+=1
while y:
    st2 = stringformer(cntr2)
    if compare(Fs, st2) == 2:
        S3=st2
        y = False
    cntr2+=1
print(cntr1-1,cntr2-1, sep='\t')
print(Fs)
print(S2)
print(S3)

