class MyCalendar:

    def __init__(self):
        self.cal = [(0, 0), (10**9, 10**9)]

    def book(self, start: int, end: int) -> bool:
        left, right = 0, len(self.cal)
        while left < right:
            mid = (left+right)//2
            if end == self.cal[mid][0]:
                left = mid
                break
            
            elif end > self.cal[mid][0]:
                left = mid + 1
            
            else:
                right = mid

        if start < self.cal[left-1][1]: return False
        self.cal.insert(left, (start, end))
        return True
        

# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
interval = [[10, 20], [15, 25], [20, 30]]
for start, end in interval:
    param_1 = obj.book(start,end)
    print(param_1)