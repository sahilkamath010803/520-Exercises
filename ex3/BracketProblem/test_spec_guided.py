import pytest
from solution import solve_bracket  

pytestmark = pytest.mark.spec_guided

# -----------------------------
# Specification 1: Total Balance Rule (cnt1 != cnt4 => res == 0)
# -----------------------------
def test_spec1_balance_mismatch_1():
    assert solve_bracket(2, 0, 0, 1) == 0

def test_spec1_balance_mismatch_2():
    assert solve_bracket(1, 0, 0, 0) == 0

# -----------------------------
# Specification 2: Traversal/Buffer Rule (cnt1 == 0 and cnt3 != 0 => res == 0)
# -----------------------------
def test_spec2_traversal_rule_1():
    assert solve_bracket(0, 0, 2, 0) == 0

def test_spec2_traversal_rule_2():
    assert solve_bracket(0, 0, 5, 0) == 0

# -----------------------------
# Specification 3: Valid Case (cnt1 == cnt4 and valid traversal => res == 1)
# -----------------------------
def test_spec3_valid_case_1():
    assert solve_bracket(1, 0, 0, 1) == 1

def test_spec3_valid_case_2():
    assert solve_bracket(3, 0, 0, 3) == 1

def test_spec3_edge_case_zero():
    assert solve_bracket(0, 0, 0, 0) == 1  # Valid by spec

def test_spec3_with_cnt2():
    assert solve_bracket(2, 5, 0, 2) == 1

# -----------------------------
# Specification 4: Error Handling - Negative Inputs
# -----------------------------
def test_spec4_negative_input_1():
    with pytest.raises(ValueError):
        solve_bracket(-1, 0, 0, 0)

def test_spec4_negative_input_2():
    with pytest.raises(ValueError):
        solve_bracket(0, -2, 0, 0)

def test_spec4_negative_input_4():
    with pytest.raises(ValueError):
        solve_bracket(0, 0, 0, -4)

# -----------------------------
# Specification 5: Error Handling - Type Checking
# -----------------------------
def test_spec5_type_check_string():
    with pytest.raises(TypeError):
        solve_bracket(0, 'abc', 0, 0)

def test_spec5_type_check_float():
    with pytest.raises(TypeError):
        solve_bracket(0, 3.5, 0, 0)

def test_spec5_multiple_invalid_types():
    with pytest.raises(TypeError):  # Should still fail on one of them
        solve_bracket('x', [1], 0, 10)

# -----------------------------
# Additional Edge Cases for Coverage
# -----------------------------
def test_edge_case_all_zero():
    assert solve_bracket(0, 0, 0, 0) == 1

def test_edge_case_large_inputs():
    assert solve_bracket(100, 200, 0, 100) == 1

def test_edge_case_cnt2_only():
    assert solve_bracket(0, 5, 0, 0) == 1  # Only cnt2 used

def test_edge_case_cnt1_zero_and_cnt3_zero():
    assert solve_bracket(0, 0, 0, 0) == 1