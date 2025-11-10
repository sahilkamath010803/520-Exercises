#Qwen Failed2 test
def func2(cnt1, cnt2, cnt3, cnt4):
    
    # NEW BRANCH:
    # This is a new guard clause to handle invalid inputs.
    # The JSON tests ("1 2 3 4", "0 0 0 0", etc.) all use non-negative numbers.
    # This branch will be "missed" by current test file.
    if cnt1 < 0 or cnt2 < 0 or cnt3 < 0 or cnt4 < 0:
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