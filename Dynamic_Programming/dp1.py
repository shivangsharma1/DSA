def bruteforce(n):
    if n<=1:
        return 1
    return bruteforce(n-1) +  bruteforce(n-2)

print("Brute force", bruteforce(5))


def memoization(n, hashmap):
    if n<=1: return 1
    if n in hashmap: return hashmap[n]

    hashmap[n] = memoization(n-1, hashmap) + memoization(n-2, hashmap)

    return hashmap[n]


print("Memoization", memoization(5, {}))