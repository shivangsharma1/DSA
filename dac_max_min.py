def dac_max_min(arr, low, high):
    max_val = arr[low]
    min_val = arr[low]

    if low == high:
        return max_val, min_val
    
    elif low == high-1:
        if arr[high]>arr[low]:
            max_val = arr[high]
            min_val = arr[low]
        else:
            max_val = arr[low]
            min_val = arr[high]

        return max_val, min_val
    
    else:
        mid = low + (high-low)//2
        max1, min1 = dac_max_min(arr, low, mid)
        max2, min2 = dac_max_min(arr, mid+1, high)

    return max(max1, max2), min(min1, min2)





if __name__ == '__main__':
    arr = [50, 90, 170, 25, 15, 7, 190, 4, 59]
    low = 0
    high = len(arr) - 1
    print(dac_max_min(arr, low, high))