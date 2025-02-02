# * https://leetcode.com/problems/min-stack/


class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)
        self._stack.append(val)

    def pop(self) -> None:
        val = self._stack.pop()
        if val == self._min_stack[-1]:
            self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]


minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(minStack.getMin()); # return -3
minStack.pop();
print(minStack.top());    # return 0
print(minStack.getMin()); # return -2