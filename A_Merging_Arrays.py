t1,t2= map(int, input().split())

ans1 = list(map(int, input().split()))
ans2 = list(map(int, input().split()))
ans = sorted(ans1+ans2)

print(*ans)
