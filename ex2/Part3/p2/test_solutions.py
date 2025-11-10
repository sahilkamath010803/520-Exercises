from buggy_solutions import func2
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
        
def test_bracket_invalid_type_input():
    with pytest.raises(TypeError):
        func2(1, 2.5, 3, 4)
        
def test_bracket_negative_input():
    with pytest.raises(ValueError, match="Counts must be non-negative"):
        func2(-1, 0, 0, 0)
        
def test_func2_invalid_types_raise_typeerror():
    with pytest.raises(TypeError):
        func2(1, 2, 3, '4')

def test_func2_negative_inputs_raise_valueerror():
    with pytest.raises(ValueError):
        func2(-1, 2, 3, 4)

def test_func2_all_conditions_met_returns_1():
    assert func2(5, 0, 0, 5) == 1

def test_func2_total_balance_broken_returns_0():
    assert func2(2, 0, 1, 3) == 0

def test_func2_traversal_balance_broken_returns_0():
    assert func2(0, 2, 3, 0) == 0

def test_func2_large_numbers_success():
    assert func2(10**6, 0, 0, 10**6) == 1