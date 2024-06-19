def intersection(arr1, arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)

    if len(arr1)<=len(arr2):
        return [ele for ele in arr1 if ele in arr2]
    else:
        return [ele for ele in arr2 if ele in arr1]



if __name__ =='__main__':
    arr1 = [2, 4, 6, 8, 11, 13]
    arr2 = [1, 3, 4, 6]

    result = intersection(arr1, arr2)

    print(result)