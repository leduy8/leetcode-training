
# * https://leetcode.com/problems/valid-parentheses/

class Stack:
    def __init__(self) -> None:
        self._arr = []
        self._size = 0

    def push(self, item):
        self._arr.append(item)
        self._size += 1

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'

        pop = self._arr.pop()
        self._size -= 1

        return pop

    def peek(self):
        if self.is_empty():
            return 'Stack is empty'

        return self._arr[-1]

    def is_empty(self):
        return self._size <= 0


def isValid(s: str) -> bool:
    stack = Stack()

    for c in s:
        if is_left_bracket(c):
            stack.push(c)
        elif is_right_bracket(c):
            item = stack.pop()
            if item == 'Stack is empty':
                return False
            if not is_match_brackets(item, c):
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
    valid_parentheses = [('[', ']'), ('{','}'), ('(', ')'), ('<', '>')]
    return True if (left, right) in valid_parentheses else False


print(isValid('()')) # True
print(isValid('()[]{}')) # True
print(isValid('(]')) # False
print(isValid('([)]')) # False
print(isValid('{[]}')) # True
print(isValid(')')) # False
print(isValid('[')) # False
