import sys
t= int(input())

for i in range(t):
    current =[]
    x,y = map(int, input().split())
    for i in range(x):
        current.append(input())
    for i in range(y):
        c =input().split()
        print(c[0],c[1])
    sys.exit()