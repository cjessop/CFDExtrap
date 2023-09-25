import numpy as np
from CFD_Extrap import finite_diff

# Test case 1
M_old = [1, 2, 3, 4, 5]
M_current = [2, 3, 4, 5, 6]
expected_output = np.array([-1, -1, -1, -1, -1])
assert np.allclose(finite_diff(M_old, M_current), expected_output)

# Test case 2
M_old = [1, 2, 3, 4, 5]
M_current = [1, 2, 3, 4, 5]
expected_output = np.array([0, 0, 0, 0, 0])
assert np.allclose(finite_diff(M_old, M_current), expected_output)

# Test case 3
M_old = [1, 2, 3, 4, 5]
M_current = [0, 0, 0, 0, 0]
expected_output = np.array([1, 2, 3, 4, 5])
assert np.allclose(finite_diff(M_old, M_current), expected_output)

# Test case 4
M_old = [1, 2, 3, 4, 5]
M_current = [5, 4, 3, 2, 1]
expected_output = np.array([4, 2, 0, -2, -4])
assert np.allclose(finite_diff(M_old, M_current), expected_output)