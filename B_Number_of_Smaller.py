import sys
input_data = sys.stdin.read().split()

t1, t2 = map(int, input().split())
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
ans = []
i = 0
for x in n2:
    while i < n and n1[i] < x:
        i += 1
    ans.append(i)
print(*ans)