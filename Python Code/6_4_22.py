N, M, x = int(input()), int(input()), 0
mat = [input().split() for i in range(N)]
P = [i for i in input()]
def check(lis, P):
    for j in P:
        if j not in lis:
            return False
    return True
def vibu(lis):
    lis.sort()
    for i in lis:
        print(i,end = '')
    print('\nLucky Player')
for i in mat:
    if check(i, P):
        vibu(i)
        x = 1
temp = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
for i in temp:
    if check(i, P):
        vibu(i)
        x = 1
if x ==0:
    print('Unlucky Player')

#Test case
# 3
# 4
# Q W E R
# A S D F
# Z X C V
# QZA
