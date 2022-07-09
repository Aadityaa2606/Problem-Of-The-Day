p1 = input(' ')
p2 = input(' ')
p3 = input(' ')
p4 = input(' ')

def discalc(a, b):
    x1 = int(a[0])
    y1 = int(a[2])
    x2 = int(b[0])
    y2 = int(b[2])
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

p1p2 = discalc(p1, p2)
p2p3 = discalc(p2, p3)
p3p4 = discalc(p3, p4)
p1p4 = discalc(p1, p4)

if p1p2 == p3p4 and p2p3 == p3p4:
    print('Yes')
else:
    print('No')