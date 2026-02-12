nums = list(map(int,input().split()))
sum = 0
for i in range(1,nums[2]+1):
    sum+=nums[0]*i

if sum >= nums[1]:
    print(sum-nums[1])
else:
    print(0)