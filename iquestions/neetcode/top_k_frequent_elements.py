from collections import Counter

def topKFrequent(nums, k):
    print("NUms length", len(nums))
    print("NUms arr: ", nums)
    freq_arr = [[] for l in range(len(nums)+1)]
    print("freq arr length", len(freq_arr))
    counter = {}
    for i in nums:
        counter[i] = 1+counter.get(i, 0)

    print("counter: ",counter)

    for element, freq in counter.items():
        freq_arr[freq].append(element)

    print("freq_arr: ",freq_arr)

    res = []
    for i in range(len(freq_arr)-1, 0, -1):
        for j in freq_arr[i]:
            res.append(j)
            if len(res)==k:
                return res

nums = [1,1,1,2,2,3,4,4,4,4,4]
# nums = [1,1,1,2,2,3]
print(topKFrequent(nums, 2))
