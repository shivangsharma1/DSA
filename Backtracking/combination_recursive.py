def combination(n, k):
    curcomb, comb = [], []
    helper(1, curcomb, comb, n, k)
    return comb


def helper(i, curcomb, comb, n, k):
    if i>n:
        return
    
    if len(curcomb) == k:
        comb.append(curcomb.copy())

    curcomb.append(i)
    helper(i+1, curcomb, comb, n, k)
    curcomb.pop()
    helper(i+1, curcomb, comb, n, k) 
    