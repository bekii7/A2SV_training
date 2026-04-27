t= int(input()  )
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    min_char = min(s)
    idx = -1
    for i in range(n):
        if s[i] == min_char:
            idx = i
    result = s[idx] + s[:idx] + s[idx+1:]
    
    print(result)