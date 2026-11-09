def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code
    mp = {}
    for c,t in zip(categories,targets):
        if mp.get(c):
            mp[c][0]+=t
            mp[c][1]+=1
        else:
            mp[c] = [t,1]
    ans = []
    for c in categories:
        ans.append(mp[c][0]/mp[c][1])
    return ans