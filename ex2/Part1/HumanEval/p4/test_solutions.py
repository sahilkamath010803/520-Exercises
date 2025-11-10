from solution import func1
import pytest
import json

def load_test_cases(filename):
    """A helper function to load test cases from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

# --- Test for HumanEval/3 (below_zero) ---
def test_below_zero():
    # Load the JSON file to get test cases
    test_data = load_test_cases('./p3.json')
    test_cases = [
        {'input': [], 'output': False},
        {'input': [1, 2, -3, 1, 2, -3], 'output': False},
        {'input': [1, 2, -4, 5, 6], 'output': True},
        {'input': [1, -1, 2, -2, 5, -5, 4, -4], 'output': False},
        {'input': [1, -1, 2, -2, 5, -5, 4, -5], 'output': True},
        {'input': [1, -2, 2, -2, 5, -5, 4, -4], 'output': True}
    ]
    
    for case in test_cases:
        operations = case['input']
        expected_output = case['output']
        
        # Run the function
        actual_output = func1(operations)
        
        # Check the result
        assert actual_output == expected_output, f"Failed on input {case['input']}"

