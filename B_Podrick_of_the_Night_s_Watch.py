import sys

t = int(input())
counts = {}
total_entries = 0

for _ in range(t):
    num = int(input())
    total_entries += num
    for _ in range(num):
        s, h = input().split()
        pair = s + h
        counts[pair] = counts.get(pair, 0) + 1


for pair in counts:
    if counts[pair] / t >= 0.8:
        print("YES")
        sys.exit()

print("NO")