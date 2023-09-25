import numpy as np
from CFD_Extrap import finite_diff

def test_finite_diff():
    # Test case 1
    M_old = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    M_current = 1.0
    expected_output = np.matrix([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    assert np.allclose(finite_diff(M_old, M_current), expected_output)

    # Test case 2
    M_old = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    M_current = 1.5
    expected_output = np.matrix([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    assert np.allclose(finite_diff(M_old, M_current), expected_output)

    # Test case 3
    M_old = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    M_current = 2.0
    expected_output = np.matrix([0.0, 0.0, 0.0, 0.0, 0.0, 1.0])
    assert np.allclose(finite_diff(M_old, M_current), expected_output)

    # Test case 4
    M_old = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    M_current = 1.2
    expected_output = np.matrix([0.0, 1.0, 0.0, 0.0, 0.0, 0.0])
    assert np.allclose(finite_diff(M_old, M_current), expected_output)

    # Test case 5
    M_old = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    M_current = 1.3
    expected_output = np.matrix([0.0, 0.5, -0.16666667, 0.04166667, -0.00793651, 0.00119048])
    assert np.allclose(finite_diff(M_old, M_current), expected_output)

test_finite_diff()