n, m = input(), int(input())
n1 = n[len(n)-m:]
num = list(map(int, [i for i in n1]))
x = True
while x:
    temp = 0
    for i in range(1,m+1):
        temp += num[-i]
    num.append(temp)
    if num[-1] ==  int(n1):
        x = False
        print("Generated")
    if num[-1] > int(n1):
        x = False
        print("Cannot be generated")

