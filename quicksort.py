def partition(a, low, high):
    pivot = a[low]
    i = low

    for j in range(low+1, high+1):
        if a[j]<=pivot:
            i+=1
            a[i], a[j] = a[j], a[i]
    a[low], a[i] = a[i], a[low]
    return i

def quicksort(a, p, q):
    if p==q:
        return a
    if p<q:
        m = partition(a, p, q)
        quicksort(a, p, m-1)
        quicksort(a, m+1, q)


if __name__ =='__main__':
    a = [50, 20, 40, 90, 88, 11, 13]
    p = 0
    q = len(a)-1
    print(a)

    quicksort(a, p, q)
    print(a)
