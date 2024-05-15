from collections import deque

class Stack:
    """
    Class stack.
    """
    def __init__(self):
        self.stack = deque()

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def push(self, value):
        """
        Adds to the top of the stack. In the context of the Stack class implemented using a deque,
        the end of the deque is considered to be the top of the stack.
        """
        self.stack.append(value)

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def reverse_string(s):
    """
    Function reverses string.
    """
    stack = Stack()
    for c in s:
        stack.push(str(c))

    result = ''
    while stack.size()!=0:
        result += stack.pop()
    return result

def is_match(ch1, ch2):
    match_dict = {
    ')': '(',
    ']': '[',
    '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(s):
    stk = Stack()
    opens = ['{', '[', '(']
    closes = ['}', ']', ')']

    for c in s:
        if c in opens:
            stk.push(c)
        if c in closes:
            if stk.size() == 0:
                return False
            if not is_match(c, stk.pop()):
                return False
    return stk.size()==0

if __name__ == '__main__':

    print(reverse_string("We will conquere COVID-19"))
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
