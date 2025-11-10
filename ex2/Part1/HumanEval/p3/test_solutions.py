from solution import func1
import pytest
import json

def load_test_cases(filename):
    """A helper function to load test cases from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

# --- Test for HumanEval/11 (string_xor) ---
def test_string_xor():
    # Load the JSON file to get test cases
    test_data = load_test_cases('./p11.json')
    test_cases = [
        {'input': ('111000', '101010'), 'output': '010010'},
        {'input': ('1', '1'), 'output': '0'},
        {'input': ('0101', '0000'), 'output': '0101'}
    ]
    
    for case in test_cases:
        a, b = case['input']
        expected_output = case['output']
        
        # Run the function
        actual_output = func1(a, b)
        
        # Check the result
        assert actual_output == expected_output, f"Failed on input {case['input']}"

