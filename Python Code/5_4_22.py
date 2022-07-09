l = [int(i) for i in input().split()]
s = int(sum(l)/4)
c = s-l[0]-l[9]
a = l[1]-c
b = l[0]-a
e = l[8]-c
d = l[9]-e
print(a,b,c,d,e)