import sys

# Using sys.stdin.read for faster input handling in competitive programming
input_data = sys.stdin.read().split()

n, m = int(input_data[0]), int(input_data[1])
n1 = list(map(int, input_data[2 : n + 2]))
n2 = list(map(int, input_data[n + 2 :]))

ans = []
i = 0


for x in n2:

    while i < n and n1[i] < x:
        i += 1

    ans.append(i)

print(*ans)