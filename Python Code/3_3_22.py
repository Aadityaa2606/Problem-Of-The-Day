M = int(input(''))
N = int(input(''))
m = (bin(M)[2:])[::-1]
n = (bin(N)[2:])[::-1]
m+='0'*(32-len(m))
n+='0'*(32-len(n))
common = ''
for i in range(max(len(m),len(n))):
    if i < min(len(m),len(n)):
        if m[i] == n[i]:
            common += str(i+1) + ' '
print(common)