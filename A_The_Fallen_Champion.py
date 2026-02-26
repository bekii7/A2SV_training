import sys
win,time = map(int, input().split())

worrior_num = int(input())

for i in range(worrior_num):
    wWin,Wtime = map(int, input().split())
    if wWin >win:
        print("The Fallen Champion")
        sys.exit()
    elif wWin == win and time >Wtime:
        print("The Fallen Champion")
        sys.exit()

print("The Champion Saves the Accused")