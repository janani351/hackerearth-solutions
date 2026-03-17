import sys

def solve():
    # Read number of test cases
    try:
        line = sys.stdin.readline()
        if not line:
            return
        t = int(line.strip())
    except ValueError:
        return

    for _ in range(t):
        # Read N (length) and K (number of substrings)
        try:
            n, k = map(int, sys.stdin.readline().split())
            s = sys.stdin.readline().strip()
        except ValueError:
            continue
        
        # Count distinct characters
        distinct_chars = len(set(s))
        
        # Check if we can have K distinct starting letters
        if distinct_chars >= k:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()

