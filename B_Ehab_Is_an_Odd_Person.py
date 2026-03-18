t= int(input())

nums = list(map(int, input().split()))
nums.sort()
for i in range(t):
    print(nums[i],end=" ")
