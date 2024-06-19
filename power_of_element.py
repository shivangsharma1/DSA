def dac_power_element(a, n):
    if n == 1:
        return a
    else:
        mid = n//2
        left = dac_power_element(a, mid)
        total = left*left
    
    if n%2==0:
        return total
    else:
        return total*a



if __name__ =='__main__':
    a = 2
    n = 64
    result  = dac_power_element(a, n)
    print(result)