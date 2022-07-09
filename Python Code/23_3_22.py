m = int(input(''))
n = int(input(''))

chk=True
while chk and n>0:
    if (2*n)%(m+1)==0:
        NPerVillage=(4*n)/(m+1)
    n-=1

print(n)
print(NPerVillage)
