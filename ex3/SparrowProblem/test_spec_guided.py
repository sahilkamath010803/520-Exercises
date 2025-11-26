import pytest
from solution import solve_sparrow

# Specification 1: The "Always Full" Case
def test_spec_guided_always_full_case_1():
    assert solve_sparrow(0, 5) == 0
    
def test_spec_guided_always_full_case_2():
    assert solve_sparrow(3, 5) == 3
    
def test_spec_guided_always_full_case_3():
    assert solve_sparrow(5, 5) == 5

# Specification 2: The "Two-Phase" Case (Corrected Logic)
def test_spec_guided_two_phase_case_1():
    # n=6, m=5 -> remaining=1, sparrow_consumption=1 when k=1 => res=6
    assert solve_sparrow(6, 5) == 1 + 5  # n=6, m=5 => remaining=1, k=1, res=6
    
def test_spec_guided_two_phase_case_2():
    # n=15, m=5 -> remaining=10
    # k=4 -> (4*5)/2 = 10 => res=9
    assert solve_sparrow(15, 5) == 9
    
def test_spec_guided_two_phase_case_3():
    # n=16, m=5 -> remaining=11
    # k=4 -> (4*5)/2 = 10 < 11, k=5 -> (5*6)/2 = 15 >= 11 => res=10
    assert solve_sparrow(16, 5) == 10

# Specification 3: Error Handling (Defensive Coding)
def test_spec_guided_error_handling_m_less_1():
    with pytest.raises(ValueError):
        solve_sparrow(5, 0)
        
    with pytest.raises(ValueError):
        solve_sparrow(5, -1)
        
def test_spec_guided_error_handling_n_less_0():
    with pytest.raises(ValueError):
        solve_sparrow(-5, 3)
        
def test_spec_guided_error_handling_invalid_types():
    with pytest.raises(TypeError):
        solve_sparrow("5", 5)
        
    with pytest.raises(TypeError):
        solve_sparrow(5, "5")