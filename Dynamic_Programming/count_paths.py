# TC and SC = O(2^(m+n))

def brute_force(r, c, row, col):
    if r >= row or c>=col:
        return 0
    
    if r == row-1 and c == col-1:
        return 1
    
    return brute_force(r+1, c, row, col) + brute_force(r, c+1, row, col)

print("brute force",brute_force(0, 0, 4, 4))


#=====================================================================================
#memoization
# TC and SC = O(n * m)
def memoization(r, c, row, col, cache):
    if r>=row or c >= col:
        return 0
    if r==row-1 and c==col-1:
        return 1
    if cache.get((r,c), 0) > 0:
        return cache[(r, c)]

    
    cache[(r, c)] = memoization(r+1, c, row, col, cache) + memoization(r, c+1, row, col, cache)
    return cache[(r,c)]

print("Memoization: ",memoization(0, 0, 4, 4, {}))

#=====================================================================================
#dynamic programming soln

def count_paths(m, n):
    row = [0] * n

    for _ in range(m-1, -1, -1):
        newrow = [0] * n
        newrow[-1] = 1
        for col in range(n-2, -1, -1):
            newrow[col] = newrow[col+1] + row[col]
        row = newrow

    return row[0]

print("DP: ",count_paths(4, 4))