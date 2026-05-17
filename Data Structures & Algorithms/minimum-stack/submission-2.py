class MinStack:
    #O(1) Lookup for TC
    #Space: O(N)
    def __init__(self):
        self.stack = []   
        self.min_dict = {}# Dict to map total elements -> smallest value
        self.size=0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.size+=1
        
        if self.size == 1:
            current_min = val
        else:
            last_min = self.min_dict[self.size - 1]
            current_min = min(val, last_min)
        self.min_dict[self.size] = current_min

    def pop(self) -> None:
        self.stack.pop()
        del self.min_dict[self.size]
        self.size -=1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        self.size = len(self.stack)
        if self.size==0:
            return
        return self.min_dict[self.size]


