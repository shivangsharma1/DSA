def sortedArray(a, b):
    # Write your code here
    fin = []
    k, j=0, 0
    
    if len(a) <= len(b):
        small_len = len(a)
    else:
        small_len = len(b)
    
    for i in range(small_len):
        if a[j]==b[k]:
            fin.append(a[j])
            j+=1
            k+=1
        elif a[j]<b[k]:
            fin.append(a[j])
            j+=1
        else:
            fin.append(b[k])
            k+=1
    
    if len(a)>small_len:
        for i in range(small_len-1, len(a)):
            fin.append(a[i])
    
    if len(b)>small_len:
        for i in range(small_len-1, len(b)):
            fin.append(b[i])

    return fin


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = sortedArray(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(*union)