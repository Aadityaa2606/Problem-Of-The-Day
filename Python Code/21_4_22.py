s = input()[::-1]
RA = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

val =0
chk2 = False
for i in range(4):
    x1,x2,x3 = RA[s[i]], RA[s[i+1]], RA[s[i+2]]
    if x2 == x3 and x2 < x1:
        chk2 = True
        val += x1-(x2+x3)
        s = s[(i+2):] 
if chk2:
    s = s[1:]

print(s)
print(val)
# temp = RA[s[0]]
# s2 = s
# chk = False
# for i in range(len(s)-1):
#     e1, e2 = RA[s[i]], RA[s[i+1]]
#     if e1 < e2:
#         temp += e2
#     elif e1 > e2:
#         temp -= e2
#     elif e1 == e2 and e1 != 'L' and e2 != 'L':
#         temp += e2
#     elif e1 == 'L' and e2 == 'L':
#         chk = True
    
# if chk:
#     print('Invalid')
# else:
#     print(temp+val)
