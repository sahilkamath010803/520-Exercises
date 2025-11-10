from solution import func1
import pytest
import json

def load_test_cases(filename):
    """A helper function to load test cases from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

# --- Test for HumanEval/6 (parse_nested_parens) ---
def test_parse_nested_parens():
    # Load the JSON file to get test cases
    test_data = load_test_cases('./p6.json')
    test_cases = [
        {'input': '(()()) ((())) () ((())()())', 'output': [2, 3, 1, 3]},
        {'input': '() (()) ((())) (((())))', 'output': [1, 2, 3, 4]},
        {'input': '(()(())((())))', 'output': [4]}
    ]
    
    for case in test_cases:
        paren_string = case['input']
        expected_output = case['output']
        
        # Run the function
        actual_output = func1(paren_string)
        
        # Check the result
        assert actual_output == expected_output, f"Failed on input {case['input']}"

