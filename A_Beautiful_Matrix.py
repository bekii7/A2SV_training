matrix = [list(map(int, input().split())) for _ in range(5)]

for r in range(5):
    for c in range(5):
        if matrix[r][c] == 1:
            ans = abs(r - 2) + abs(c - 2)
            print(ans)
            break