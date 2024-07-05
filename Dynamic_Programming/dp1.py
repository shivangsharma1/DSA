def bruteforce(n):
    if n<=1:
        return 1
    return bruteforce(n-1) +  bruteforce(n-2)

print("Brute force", bruteforce(5))


    