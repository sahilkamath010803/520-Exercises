def func1(n, m):

    if m < 1:
        raise ValueError("m must be 1 or greater")
    if n <= m:
        return n 
    else:
        remaining = n - m
        left = 1
        right = 2 * 10 ** 9
        while left < right:
            mid = (left + right) >> 1
            if mid * (mid + 1) // 2 < n - m:
                left = mid + 1
            else:
                right = mid
        return m + left