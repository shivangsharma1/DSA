from collections import Counter


#using map
def topKelementmap(arr, k):
    mp = {}
    for i in arr:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
    a = [0] * len(mp)
    j=0
    for i in mp:
        a[j] = [i,mp[i]]
        j+=1

    a = sorted(a, key=lambda x: x[1], reverse=True)
    print(a)
    res = []
    for i in range(k):
        res.append(a[i][0])
    
    return res


import heapq
def topKelementheap(arr, k):
    mp = {}
    for i in arr:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1

    heap = [[value, key] for key, value in mp.items()]

    largest = heapq.nlargest(k, heap)
    res = []
    for i in range(k):
        res.append(largest[i][1])

    return res

if __name__ =='__main__':
    arr = [7, 8, 8, 10, 8, 9, 11, 7]
    k = 2
    result = topKelementheap(arr, k)
    print(result)