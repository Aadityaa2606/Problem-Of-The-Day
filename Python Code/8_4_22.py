# n, col, m, oder = int(input()), input().split(), int(input()), input()

# def check(m, strg):
#     while len(strg) > 1:
#         x = strg[:(m+1)]
#         if (x[0] in x[1:]):
#             return False
#         strg = strg[1:]
#     return True

# if check(m, oder):
#     print('Valid')
# else:
#     print('Invalid')

# # strh = 'hii'
# # print(strh)
# # strh = strh[1:]
# # print(strh)

n, nums = int(input()), list(map(int ,input().split()))
nums.append(max(nums)+1)
chk = 0
for i in range(n):
    if nums[i] > nums[i+1]:
        chk+=1
    
if chk == 0:
    print('Correct')
elif chk == 1:
    print('Easily correctable')
else:
    print('Not easily correctable')
