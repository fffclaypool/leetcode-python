class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }

        stack = []

        for token in tokens:
            if token in operations:
                y = stack.pop()
                x = stack.pop()
                operation = operations[token]
                stack.append(operation(x, y))
            else:
                stack.append(int(token))
        return stack.pop()
