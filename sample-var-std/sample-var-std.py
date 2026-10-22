import numpy as np
import math

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    n = len(x)
    mean = sum(x)/n
    total = 0
    for i in x:
        total+=math.pow(i-mean,2)
    res={}
    res["variance"] = float(total/(n-1))
    res["standard_deviation"] = math.sqrt(res["variance"])
    return res