w1 = input('')[::-1]
w2 = input('')[::-1]
w3 = ''
code = ''
# print(ord('z')-97)
maximum = max(len(w1), len(w2))
up = w1
dwn = w2
if len(w2) == maximum:
    up = w2
    dwn = w1
dwn += 'a'*(len(up)-len(dwn))

carry = 0
add = 0

for i in range(len(up)):
    add = ord(up[i])-97+ord(dwn[i])-97+carry
    carry = add//10
    w3 += str(add%10)
if is for in 

w3 += str(carry)
print(up)
print(dwn) 
print(w3[::-1])

