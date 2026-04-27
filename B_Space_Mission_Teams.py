import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    d = int(input_data[1])
    p = sorted(list(map(int, input_data[2:])), reverse=True)
    
    left = 0       
    right = n - 1    
    ans = 0
    
    while left <= right:
        max_skill = p[left]
        
      
        needed_count = (d // max_skill) + 1
        
      
        if (right - left + 1) >= needed_count:
            ans += 1
            right -= (needed_count - 1)
            left += 1
        else:
            break
            
    print(ans)

if __name__ == "__main__":
    solve()