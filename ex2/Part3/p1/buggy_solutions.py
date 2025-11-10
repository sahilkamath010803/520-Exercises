def func1(n, m):
    # Case 1: n is too small to run out at any point
    if n <= m:
        return 0  # Never runs out

    left, right = 1, 2 * 10**18  # Large enough range

    def used(k):
        # Total used on k days = sum_{i=1}^k i = k*(k+1)/2
        # Extra grain added = m*(k-1)
        return k * (k + 1) // 2 - m * (k - 1)

    while left < right:
        mid = (left + right) // 2
        if used(mid) < n:
            left = mid + 1
        else:
            right = mid

    return left