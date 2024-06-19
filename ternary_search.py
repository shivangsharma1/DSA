def ternary_search(arr, ele, i, j):
    while i <= j:
        mid1 = i + (j - i) // 3
        if arr[mid1] == ele:
            return mid1

        mid2 = j - (j - i) // 3
        if arr[mid2] == ele:
            return mid2

        if ele < arr[mid1]:
            return ternary_search(arr, ele, i, mid1 - 1)

        elif ele > arr[mid2]:
            return ternary_search(arr, ele, mid2 + 1, j)

        else:
            return ternary_search(arr, ele, mid1 + 1, mid2 - 1)


# dirver code
arr = [20, 25, 47, 56, 59, 63, 65, 79, 82]
ele = 92
i = 0
j = len(arr) - 1
print(ternary_search(arr, ele, i, j))
