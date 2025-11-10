from solution import func2
import pytest
import json

def load_test_cases(filename):
    """A helper function to load test cases from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

# --- Test for Bracket Problem (APPS/Bracket) ---
def test_bracket_problem():
    # Assuming you create a 'bracket_tests.json'
    test_cases = load_test_cases('./test_cases.json') 
    for case in test_cases:
        input_str = case['input']
        expected_output = str(case['output'])
        
        # Parse "1 2 3 4" into (1, 2, 3, 4)
        cnt1, cnt2, cnt3, cnt4 = map(int, input_str.split())
        
        # Run the function
        actual_output = str(func2(cnt1, cnt2, cnt3, cnt4))
        
        # Check the result
        assert actual_output == expected_output, f"Failed on input {input_str}"