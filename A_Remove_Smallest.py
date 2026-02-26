def solve():
    num = int(input())
    nums = sorted(list(map(int, input().split())))
    
    for i in range(1, num):
        if nums[i] - nums[i-1] > 1:
            print("NO")
            return
            
    print("YES")

t = int(input())
for i in range(t):
    solve()