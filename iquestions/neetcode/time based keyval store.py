from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.dic[key]
        res = ""
        left, right = 0, len(values) - 1
        while left<=right:
            mid = (left+right)//2
            if values[mid][1]<=timestamp:
                res = values[mid][0]
                left = mid+1
            else:
                right = mid-1

        return res

        


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo","bar",1)
param_2 = obj.get("foo",1)
print(param_2)

param_3 = obj.get("foo",3)
print(param_3)

obj.set("foo","bar2",4)



