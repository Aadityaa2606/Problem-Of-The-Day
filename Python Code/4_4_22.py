m = int(input())
mval = input().split(' ')
n = int(input())
nval = input().split(' ')
for i in nval:
    mval.append(i)
m1 = [int(i) for i in mval if int(i)%5 ==0]
m1.sort()
m2 = [int(i) for i in mval if int(i)%5 !=0]
m2.sort()
for i in m1:
    print(i, end=' ')
print('')
for i in m2:
    print(i, end=' ') 

# 7
# 12 17 20 27 29 31 35
# 6
# 30 28 25 23 16 5
