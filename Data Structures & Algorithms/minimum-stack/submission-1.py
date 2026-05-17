class MinStack:
    #O(1) Lookup for TC
    #Space: O(N)
    def __init__(self):
        # Maps: index: (actual_value, current_min)
        self.stack_dict = {}
        self.size = 0

    def push(self, val: int) -> None:
        if self.size == 0:
            current_min = val
        else:
            prev_min = self.stack_dict[self.size - 1][1]
            current_min = min(val, prev_min)
        self.stack_dict[self.size] = (val, current_min)
        self.size += 1

    def pop(self) -> None:
        # Reduce the size and delete the top index entry
        self.size -= 1
        del self.stack_dict[self.size]

    def top(self) -> int:
        # The top element is always at index (size - 1)
        return self.stack_dict[self.size - 1][0]

    def getMin(self) -> int:
        # The minimum for the current stack state is stored at index (size - 1)
        return self.stack_dict[self.size - 1][1]