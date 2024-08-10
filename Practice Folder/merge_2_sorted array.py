# Python program to merge two sorted arrays/
def mergeArrays(arr1, arr2, n1, n2, arr3):
    i = 0
    j = 0
    k = 0

    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            arr3[k] = arr1[i]
            i+=1
            k+=1
        else:
            arr3[k] = arr2[j]
            j+=1
            k+=1

    if i<len(arr1):
        arr3[k] = arr1[i]
        k+=1
        i+=1

    if j<len(arr1):
        arr3[k] = arr2[j]
        k+=1
        j+=1
    
    print(arr3)

# Driver code
if __name__ == '__main__':
    arr1 = [1, 3, 5, 7]
    n1 = len(arr1)

    arr2 = [2, 4, 6, 8]
    n2 = len(arr2)

    arr3 = [0] * (n1+n2)
    mergeArrays(arr1, arr2, n1, n2, arr3)
