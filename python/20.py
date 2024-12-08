
# * https://leetcode.com/problems/valid-parentheses/

class Stack:
    def __init__(self) -> None:
        self.arr = []
        self.size = 0

    def push(self, item):
        self.arr.append(item)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'

        pop = self.arr.pop()
        self.size -= 1

        return pop

    def peek(self):
        if self.is_empty():
            return 'Stack is empty'

        return self.arr[-1]

    def is_empty(self):
        return self.size <= 0


def isValid(s: str) -> bool:
    stack = Stack()

    for ch in s:
        if is_left_bracket(ch):
            stack.push(ch)
        elif is_right_bracket(ch):
            item = stack.pop()
            if item == 'Stack is empty':
                return False
            if not is_match_brackets(item, ch):
                return False

    if not stack.is_empty():
        return False

    return True


def is_left_bracket(ch):
    left_brackets = ['{', '(', '[', '<']
    return True if ch in left_brackets else False


def is_right_bracket(ch):
    right_brackets = ['}', ')', ']', '>']
    return True if ch in right_brackets else False


def is_match_brackets(left, right):
    left_brackets = ['{', '(', '[', '<']
    right_brackets = ['}', ')', ']', '>']
    return True if left_brackets.index(left) == right_brackets.index(right) else False


print(isValid('()'))
print(isValid('()[]{}'))
print(isValid('(]'))
print(isValid('([)]'))
print(isValid('{[]}'))
print(isValid(')'))
print(isValid('['))
