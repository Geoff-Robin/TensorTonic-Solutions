import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    res = 0
    for x_i,p_i in zip(x,p):
        res = res + x_i*p_i
    return float(res)