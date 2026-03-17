import sys

def solve():
    # Precompute primes using Sieve up to 1,000,000
    MAX = 1000001
    is_prime = [True] * MAX
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(MAX**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, MAX, p):
                is_prime[i] = False

    # Read number of test cases
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        t = int(line1.strip())
    except ValueError:
        return

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        arr = list(map(int, sys.stdin.readline().split()))
        
        count_ones = 0
        count_primes = 0
        
        for x in arr:
            if x == 1:
                count_ones += 1
            elif x < MAX and is_prime[x]:
                count_primes += 1
        
        # Calculate combinations: (count_ones choose 2) * count_primes
        if count_ones < 2:
            print(0)
        else:
            ans = (count_ones * (count_ones - 1) // 2) * count_primes
            print(ans)

if __name__ == "__main__":
    solve()

