from collections import defaultdict

def groupanagram(strs):
    res = defaultdict(list)

    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c)-ord('a')] += 1
        print(count)
        res[tuple(count)].append(s)
    print(res)
    return res.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupanagram(strs))