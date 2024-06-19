def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def bubble_sort2(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


#Driver Code
arr = [70, 20, 50, 60, 3, 47]
result = bubble_sort2(arr)
print(result)