n = int(input(' '))
lis = input('').split(' ')
repeat = 0
for i in range(len(lis)):
    lis[i] = int(lis[i]) 
    if lis.count(lis[i]) == 2:
        repeat = lis[i]

out=[lis[0]]
d=1
mode='Happy'
num1=lis[0]
num2=lis[1]

while d != 0 and mode != 'Angry':
    d = abs(num1-num2)
    num1 = lis[d-1]
    num2 = lis[d]
    if d!=0:
        if (num1 in out) and num1 != repeat:
            mode = 'Angry'
        out.append(num1)

for i in out:
    print(i, end=' ')
print('')
print(mode)
'''
8
34 39 33 37 37 35 38 36 
'''