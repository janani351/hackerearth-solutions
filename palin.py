import sys

def solve():
    try:
        # Read n (rows) and m (columns)
        line = sys.stdin.readline().split()
        if not line: return
        n, m = map(int, line)
        
        # Initialize garden (0: empty, 1: broken)
        v = [[0 for _ in range(m)] for _ in range(n)]
        
        # Read number of broken pots
        q_line = sys.stdin.readline().split()
        if not q_line: return
        q = int(q_line[0])
        
        # Mark broken pots
        for _ in range(q):
            r, c = map(int, sys.stdin.readline().split())
            if 0 <= r < n and 0 <= c < m:
                v[r][c] = 1
                
        c1 = 0 # Max plants
        c2 = 0 # Min plants
        
        # Calculate max plants (c1)
        for i in range(n):
            length = 0
            for j in range(m):
                if v[i][j] == 0:
                    length += 1
                else:
                    c1 += (length + 1) // 2
                    length = 0
            c1 += (length + 1) // 2
            
        # Calculate min plants (c2)
        for i in range(n):
            length = 0
            for j in range(m):
                if v[i][j] == 0:
                    length += 1
                else:
                    c2 += (length + 2) // 3
                    length = 0
            c2 += (length + 2) // 3
            
        print(c1, c2)
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()

