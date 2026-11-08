import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    res = {}
    res["pmf"] = []
    for i in x:
        if i == 0:
            res["pmf"].append(1-p)
        else:
            res["pmf"].append(p)
    res["mean"] = float(p)
    res["variance"] = float(p*(1-p))
    res["pmf"] = np.array(res["pmf"])
    return res
            