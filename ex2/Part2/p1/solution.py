import pytest

def func1(n, m):
    
    # --- NEW UNTESTED BRANCHES ---

    # BRANCH 1 (Missed by baseline tests) - Type Checking
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError("Inputs n and m must be integers")
        
    # BRANCH 2 (Missed by baseline tests) - Value Check (m)
    if m < 1:
        raise ValueError("m must be 1 or greater")

    # BRANCH 3 (Missed by baseline tests) - Value Check (n)
    if n < 0:
        raise ValueError("n (capacity) must be non-negative")

    # --- ORIGINAL CORRECT CODE ---
    
    # BRANCH 4 (Also missed if you removed the "1024 1024" test)
    if n <= m:
        return n 
    else:
        remaining = n - m
        left = 1
        right = 2 * 10 ** 9 # Using the safer high bound
        while left < right:
            mid = (left + right) >> 1
            if mid * (mid + 1) // 2 < n - m:
                left = mid + 1
            else:
                right = mid
        return m + left