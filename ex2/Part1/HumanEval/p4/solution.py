from typing import List

def func1(operations: List[int]) -> bool:
    """ Detects if at any point the balance falls below zero. """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

