from typing import List
import re


def func1(paren_string: str) -> List[int]:
    """ Uses stack-based approach to calculate depth of parentheses. """
    groups = paren_string.strip().split()
    result = []
    for group in groups:
        max_depth = 0
        current_depth = 0
        for ch in group:
            if ch == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif ch == ')':
                current_depth -= 1
        result.append(max_depth)
    return result