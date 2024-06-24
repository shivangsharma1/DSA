class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while i>1 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def pop(self):
        if len(self.heap) == 1:
            return None
        
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap = self.heap.pop()
        i=1
        while 2*i < len(self.heap):
            if 2*i+1 < len(self.heap) and self.heap[2*i+1]<self.heap[2*i] and \
                self.heap[2*i+1] < self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[2*i+1]
                self.heap[i] = temp
                i = 2*i+1

            elif self.heap[i]> self.heap[2*i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[2*i]
                self.heap[2*i] = temp
                i = 2*i

            else: break

        return res
    
    def heapify(self, arr):
        arr.append(arr[0])
        self.heap = arr
        cur = (len(self.heap) - 1)//2

        while cur>0:
            i = cur
            while 2*i < len(self.heap):
                if 2*i+1 < len(self.heap) and self.heap[2*i+1] < self.heap[2*i] \
                and self.heap[2*i+1] < self.heap[i]:
                    self.heap[2*i+1], self.heap[i] = self.heap[i], self.heap[2*i+1]
                    i = 2*i+1
                elif self.heap[2*i]<self.heap[i]:
                    self.heap[2*i],self.heap[i] = self.heap[i], self.heap[2*i]
                    i = 2*i
                else:break 
            cur-=1 