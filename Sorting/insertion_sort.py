#insertion sorting code
# best case time complexity = O(n)
# worst case time complexity = 1/2 * O(n^2) = O(n^2)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        while j>=0 and arr[j+1]<arr[j]:
            arr[j+1], arr[j] = arr[j],arr[j+1]
            j-=1
    
    return arr


if __name__ == '__main__':
    arr = [55,7,4,3,7,9,4,2,]

    print(insertion_sort(arr))