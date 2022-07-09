x = int(input(''))
a = x
col = ''
while x>12:
    x -= 12
green = [1,6,12,7]
orange = [2,5,8,11]
blue = [3,4,9,10]

if x in green:
    col = 'Green'
elif x in orange:
    col = 'Orange'
else:
    col = 'Blue'

if col == 'Green':
    print(a + 11) if x == 1 else print(a+1) if x == 6 else print(a-1) if x ==7 else print(a-11)
elif col == 'Orange':
    print(a+9) if x == 2 else print(a + 3) if x == 5 else print(a-3) if x == 7 else print(a-9)
else:
    print(a+7) if x == 3 else print(a+5) if x == 4 else print(a-5) if x == 9 else print(a-7)

print(col)