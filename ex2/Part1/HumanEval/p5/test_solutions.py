from solution import func1
import pytest
import json

def load_test_cases(filename):
    """A helper function to load test cases from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

# --- Test for HumanEval/7 (filter_by_substring) ---
def test_filter_by_substring():
    # Load the JSON file to get test cases
    test_data = load_test_cases('./p7.json')
    test_cases = [
        {'input': ([], 'john'), 'output': []},
        {'input': (['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx'), 'output': ['xxx', 'xxxAAA', 'xxx']},
        {'input': (['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx'), 'output': ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']},
        {'input': (['grunt', 'trumpet', 'prune', 'gruesome'], 'run'), 'output': ['grunt', 'prune']}
    ]
    
    for case in test_cases:
        strings, substring = case['input']
        expected_output = case['output']
        
        # Run the function
        actual_output = func1(strings, substring)
        
        # Check the result
        assert actual_output == expected_output, f"Failed on input {case['input']}"

