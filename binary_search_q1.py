# input: sorted array of n distinct elements 
# output : FInd any element in an array element such that an array element and it's corresponding index is same array[i]=i. Write an optimized code. 

def find_same_index_ele_recur(arr, low, high, l):
    if low == high:
        if arr[low] == low:
            return low
        else:
            return -1
    else:
        mid = low + (high - low)//2
        if arr[mid] == mid:
            return mid
        elif arr[mid]>l:
            return find_same_index_ele_recur(arr, mid+1,high,l)
        else:
            return find_same_index_ele_recur(arr, low,high-1,l)
    




# input
arr = [1,2,3,3,4,7]
l = len(arr)
low = 0
high = l-1
print(find_same_index_ele_recur(arr, low, high, l))

