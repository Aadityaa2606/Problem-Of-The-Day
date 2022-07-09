n = int(input())
# orgi = list(map(int, input().split()))
# req = list(map(int, input().split()))
orgi = input().split()
req = input().split()
cnt = 0
for i in range(n*n):
    if orgi[i] != req[i]:
        x=req.index(orgi[i])
        temp = orgi[x]
        orgi[x] = req[x]
        orgi[i] = temp
        cnt+=1
print(cnt)
print(orgi)
print(req)
        
# temp = orgi[0]
# orgi[0] = orgi[orgi.index(req[0])]
# orgi[orgi.index(req[0])] = temp
# print(orgi[orgi.index(req[0])])
# orgi[0] = '11'
# x= orgi.index(req[0])
# print(x)
# orgi[x]='23' 
# print(temp)
# print(orgi)
# print(req)

# 3
# 23 12 45 67 53 11 13 90 75
# 11 12 13 23 45 53 67 75 90