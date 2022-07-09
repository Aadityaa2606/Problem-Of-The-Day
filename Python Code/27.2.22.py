n=int(input(''))
lis=[]
for i in range(n):
    lis.append(input(''))
string=''
for i in lis:
    if i == lis[-1]:
        string+=i[0].capitalize()+i[1:]
    else:
        string += i[0].capitalize()+i[1:]+'_'
print(string)