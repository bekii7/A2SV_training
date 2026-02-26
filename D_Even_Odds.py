n, k = map(int, input().split())
arr = []
for i in range(1,n+1):
    if i%2 != 0:
        arr.append(i)

for i in range(1,n+1):
    if i%2 == 0:
        arr.append(i)

print(arr[k-1])