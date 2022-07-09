n = int(input())
c1,c2,c3 = True
i1,i2,i3 = 0
nums = list(map(int, input().split()))
if nums[0] !=1 or nums[1] !=1:
    i1 = max(nums[0], nums[1])
    c1 = False
for i in range(2,n,2):
    if nums[i] != (nums[i-1]+nums[i-2]):
        if c2:
            i2 = nums[i]
        c2 = False
for i in range(3,n,2):
    if nums[i] != nums[int(((i+1)/2)-1)]:
        if c3:
            i3 = nums[i]
        c3 = False
if c1 == True and c2 == True and c3 == True:
    print('Yes')
elif not c1:
    print('No')
    print(i1)
elif not c2:
    print('No')
    print(i2)
elif not c3:
    print('No')
    print(i3)

