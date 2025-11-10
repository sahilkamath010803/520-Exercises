import pytest
from solution import func1
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
        
        n, m = map(int, input_str.split())
        
        actual_output = str(func1(n, m))
        
        assert actual_output == expected_output, f"Failed on input {input_str}"
        
#Added test case coverage branch #2
def test_sparrow_invalid_m_input():
    with pytest.raises(ValueError, match="m must be 1 or greater"):
        func1(5, 0)
        
#Added test case coverage branch #3
def test_sparrow_invalid_n_input():
    with pytest.raises(ValueError):
        func1(-5, 1)

#Added test case coverage branch #1        
def test_sparrow_invalid_type_input():
    with pytest.raises(TypeError):
        func1("a", 5)
    with pytest.raises(TypeError):
        func1(10, "b")
    with pytest.raises(TypeError):
        func1(5.5, 5)
    with pytest.raises(TypeError):
        func1(10, 5.5)
        

def test_func1_equal_n_and_m():
    assert func1(5, 5) == 5, "Failed when n equals m"

def test_func1_n_is_zero():
    assert func1(0, 1) == 0, "Failed when n is zero"

def test_func1_m_is_one_n_is_large():
    n = 10**18
    m = 1
    result = func1(n, m)
    assert result == m + int((2*n - m)**0.5), "Failed for large n and small m"

def test_func1_n_just_less_than_m():
    assert func1(4, 5) == 4, "Failed when n is less than m but close"

def test_func1_n_exactly_mid_square_sum():
    # Check n = sum = 1+2+...+k = k*(k+1)//2
    k = 100000
    m = 1
    n = k * (k + 1) // 2 + m
    result = func1(n, m)
    assert result == m + k, "Failed when n is exactly a triangular number plus m"

def test_func1_invalid_type_for_n():
    with pytest.raises(TypeError):
        func1("not an int", 5)

def test_func1_invalid_type_for_m():
    with pytest.raises(TypeError):
        func1(5, "not an int")

def test_func1_negative_n():
    with pytest.raises(ValueError):
        func1(-1, 5)

def test_func1_zero_m():
    with pytest.raises(ValueError):
        func1(10, 0)