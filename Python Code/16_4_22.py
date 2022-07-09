n = int(input())
nums, m = [int(input()) for i in range(n)], int(input())
def disfind(n,m):
    cntr=0
    while max(n,m)>0:
        if (n%2==0) != (m%2==0):
            cntr+=1
        n=n//2
        m=m//2
    return cntr

diff = [disfind(m,nums[i]) for i in range(n)]
mindif = min(diff)
for i in range(n):
    if diff[i] == mindif:
        print(nums[i])

# n=int(input())
# l=[]
# for i in range(n):
#     a=int(input())
#     b = bin(a)[2:]
#     l.append(int(b))
# m=int(input())
# mb=int(bin(m)[2:])
# def dif(a,b):
#     a=str(a)
#     b=str(b)
#     y=0
#     x=abs(len(a)-len(b))
#     if len(a)<len(b):
#         a='2'*x+a;
#     if len(a)>len(b):
#         b='2'*x+b;
#     for i in range(len(a)):
#         if a[i]!=b[i]:
#             y+=1
#     return y
# p=[]
# for i in l:
#     v=dif(i,mb)
#     p.append(v)
# g=min(p)
# for i in range(len(p)):
#     if p[i]==g:
#         print(l[i])