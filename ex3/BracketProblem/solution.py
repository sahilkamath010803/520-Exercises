def solve_bracket(cnt1, cnt2, cnt3, cnt4):
    
    # --- NEW UNTESTED BRANCHES ---

    # BRANCH 1 (Missed by baseline tests) - Type Checking
    inputs = [cnt1, cnt2, cnt3, cnt4]
    if not all(isinstance(i, int) for i in inputs):
        raise TypeError("All counts must be integers")

    # BRANCH 2 (Missed by baseline tests) - Value Check
    if any(i < 0 for i in inputs):
        raise ValueError("Counts must be non-negative")

    # --- ORIGINAL CORRECT CODE ---
    
    # Check the first condition: Total Balance
    if cnt1 != cnt4:
        return 0

    # Check the second condition: Traversal Balance
    if cnt1 == 0 and cnt3 != 0:
        return 0

    # If both conditions are satisfied, the string is valid
    return 1