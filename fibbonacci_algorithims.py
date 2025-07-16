"""
A few ways to compute Fibonacci numbers.
Comments include some personal thoughts and observations.
"""

from functools import lru_cache
import math

def fib_recursive(n):
    """Recursive approach. Very readable, but slow for large n."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

@lru_cache(maxsize=None)
def fib_memoized(n):
    """Recursive with memoization. Much more efficient. Python makes this very convenient."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_memoized(n-1) + fib_memoized(n-2)

def fib_iterative(n):
    """Iterative method. My default for performance—simple and fast."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_bottom_up_dp(n):
    """Bottom-up dynamic programming. Good if you want all F(0)...F(n)."""
    if n == 0:
        return 0
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]

def fib_matrix(n):
    """Matrix exponentiation. Efficient for large n, though a bit less intuitive to me at first."""
    def multiply(F, M):
        x = F[0][0]*M[0][0] + F[0][1]*M[1][0]
        y = F[0][0]*M[0][1] + F[0][1]*M[1][1]
        z = F[1][0]*M[0][0] + F[1][1]*M[1][0]
        w = F[1][0]*M[0][1] + F[1][1]*M[1][1]
        return [[x, y], [z, w]]

    def power(F, n):
        if n == 0 or n == 1:
            return F
        if n % 2 == 0:
            half = power(F, n//2)
            return multiply(half, half)
        else:
            return multiply(F, power(F, n-1))

    if n == 0:
        return 0
    F = [[1, 1], [1, 0]]
    return power(F, n-1)[0][0]

def fib_binet(n):
    """Closed-form (Binet’s formula). Elegant, but not always reliable for big n due to floating-point issues."""
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return int(round((phi**n - psi**n) / sqrt5))

if __name__ == "__main__":
    print("Comparing several methods for the first 10 Fibonacci numbers:")
    for n in range(10):
        print(f"n={n}: rec={fib_recursive(n)}, mem={fib_memoized(n)}, iter={fib_iterative(n)}, dp={fib_bottom_up_dp(n)}, mat={fib_matrix(n)}, binet={fib_binet(n)}")

    # Checking Binet’s formula for larger values
    print("\nTesting Binet’s formula on larger n (floating-point issues may appear):")
    for n in [10, 20, 50, 70]:
        print(f"n={n}: binet={fib_binet(n)}, iterative={fib_iterative(n)}")
