def combination(n, k):
    curcomb, comb = [], []
    helper(1, curcomb, comb, n, k)
    return comb

def helper(i, curcomb, comb, n, k):
    if i>=n:
        return 
    
    if len(curcomb) == k:
        comb.append(curcomb.copy())
        return
    
    for j in range(i, n+1):
        curcomb.append(j)
        helper(j+1, curcomb, comb, n, k)
        curcomb.pop()

    return comb
