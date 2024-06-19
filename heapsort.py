# def heapify(arr, n, root):
#     largest = root
#     left = (2*root) + 1
#     right = (2*root) + 2

#     if left < n and arr[left] > arr[largest]:
#         largest = left
    
#     if right < n and arr[right] > arr[largest]:
#         largest = right

#     if largest!=root:
#         arr[largest] , arr[root] = arr[root], arr[largest]
#         heapify(arr, n, largest)


def heapify(arr, n, root):
    smallest = root
    left = (2*root) + 1
    right = (2*root) + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest!=root:
        arr[smallest] , arr[root] = arr[root], arr[smallest]
        heapify(arr, n, smallest)


def heapsort(arr, n):

    for i in range((n//2)-1, -1, -1):
        heapify(arr, n , i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

if __name__ == '__main__':
    array = [75, 25, 35, 45, 90, 80, 60, 20, 30, 77, 88, 99, 11, 21, 31, 41, 5, 8, 3]
    n = len(array)
    heapsort(array, n)

    for ele in array:
        print(ele, end=" ")