from stack import Stack

brackets = {
    ')': '(',
    ']': '[',
    '}': '{',
}


def balanced(string: str) -> str:
    stack = Stack()
    for c in string:
        br1 = brackets.get(c)
        # print(f"{c=} {br1=}")
        if br1:
            if stack.is_empty() or br1 != stack.peek():
                return 'Несбалансированно'
            else:
                stack.pop()
        else:
            stack.push(c)

        # print(stack)

    if stack.is_empty():
        return 'Сбалансировано'
    else:
        return 'Несбалансированно'


bracket_list_1 = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '',
    '([][]{}{[[]]})',
]

bracket_list_2 = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]',
    '([][]{}{[[]]}()'
]

for item in bracket_list_1:
    print(balanced(item))

for item in bracket_list_2:
    print(balanced(item))
