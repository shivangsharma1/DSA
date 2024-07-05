def bruteforce(n):
    if n <= 1:
        return 1
    return bruteforce(n - 1) + bruteforce(n - 2)


print("Brute force", bruteforce(5))


# this memoization is called as DP - Top down approach
def memoization(n, hashmap):
    if n <= 1:
        return 1
    if n in hashmap:
        return hashmap[n]

    hashmap[n] = memoization(n - 1, hashmap) + memoization(n - 2, hashmap)

    return hashmap[n]


print("Memoization", memoization(5, {}))


## DP: bottom up approach , looping solution
# 
def dp(n):
    if n<=1:
        return n
    
    arr = [0, 1]
    i=2
    while i<=n:
        tmp = arr[1]
        arr[1] = arr[1] + arr[0]
        arr[0] = tmp
        i+=1

    return arr[1]
    
print("Bottom up approach", dp(5))