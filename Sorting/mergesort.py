#merge sorting code

# worst case time complexity = O(nlogn)

def merge(arr, s, m, e):
    L = arr[s:m+1]
    R = arr[m+1:e+1]

    i=j=0
    k=s
    while i<len(L) and j<len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1

    while i<len(L):
        arr[k] = L[i]
        i+=1
        k+=1

    while j<len(R):
        arr[k] = R[j]
        j+=1
        k+=1


def merge_sort(arr, s, e):
    if e - s + 1 <= 1:
        return arr
    
    mid = (s+e) // 2
    merge_sort(arr, s, mid)
    merge_sort(arr, mid+1, end)

    merge(arr, s, mid, e)
    return arr


if __name__ == '__main__':
    arr = [55,7,4,3,7,9,4,2]
    
    start, end = 0, len(arr)-1
    print(merge_sort(arr, start, end))