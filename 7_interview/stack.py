class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return False if len(self.stack) else True

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return ', '.join([str(n) for n in self.stack])


if __name__ == '__main__':
    my_stack = Stack()
    print(f"{my_stack.is_empty()=}")
    print(f"{my_stack.size()=}")

    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.push(40)

    print(f"{my_stack.size()=}")
    print(my_stack)

    print(f"{my_stack.pop()=}")
    print(my_stack)

    print(f"{my_stack.peek()=}")
    print(my_stack)

    print(f"{my_stack.pop()=}")
    print(my_stack)

    print(f"{my_stack.size()=}")
    print(f"{my_stack.is_empty()=}")
