from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    res = {}
    x.sort()
    if(len(x)%2):
        res["median"] = float(x[len(x)//2])
    else:
        mid = len(x)//2
        res["median"] = (x[mid-1]+x[mid])/2
    sum = 0
    mp={}
    for i in x:
        sum=sum+i
        if mp.get(i):
            mp[i]=mp[i]+1
        else:
            mp[i]=1
    mode = float('inf')
    max = float('-inf')
    for key,val in mp.items():
        if(max<=val):
            mode = mode if mode<key and max==val else key
            max = val
        
    mean = float(sum/len(x))
    res["mean"] = mean 
    res["mode"] = float(mode)
    return res