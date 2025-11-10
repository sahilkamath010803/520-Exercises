from solution import func1
import pytest
import json

def load_test_cases(filename):
    """A helper function to load test cases from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

# --- Test for HumanEval/5 (intersperse) ---
def test_intersperse():
    # Load the JSON file to get test cases
    test_data = load_test_cases('./p5.json')
    test_cases = [
        {'input': ([], 7), 'output': []},
        {'input': ([5, 6, 3, 2], 8), 'output': [5, 8, 6, 8, 3, 8, 2]},
        {'input': ([2, 2, 2], 2), 'output': [2, 2, 2, 2, 2]}
    ]
    
    for case in test_cases:
        numbers, delimeter = case['input']
        expected_output = case['output']
        
        # Run the function
        actual_output = func1(numbers, delimeter)
        
        # Check the result
        assert actual_output == expected_output, f"Failed on input {case['input']}"

