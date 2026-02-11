t = int(input())

for i in range(t):
    
    nums = list(map(int,input().split()))
    if max(nums) == sum(nums) - max(nums):
        print("YES")
    else:
        print("NO")