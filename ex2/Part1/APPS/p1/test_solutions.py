from solution import func1
import pytest
import json

def load_test_cases(filename):
    """A helper function to load test cases from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

# --- Test for Sparrow Problem (APPS/7) ---
def test_sparrow_problem():
    test_cases = load_test_cases('./test_cases.json')
    for case in test_cases:
        input_str = case['input']
        expected_output = str(case['output'])
        
        # Parse the input string "5 2" into (5, 2)
        n, m = map(int, input_str.split())
        
        # Run the function
        actual_output = str(func1(n, m))
        
        # Check the result
        assert actual_output == expected_output, f"Failed on input {input_str}"