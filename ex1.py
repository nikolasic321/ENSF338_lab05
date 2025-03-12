import operator

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

def evaluate_expression(expression: str):
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    stack = Stack()
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}

    def compute():
        operands = []
        while not stack.is_empty() and isinstance(stack.peek(), int):
            operands.append(stack.pop())
        op = stack.pop()
        if op not in ops:
            raise ValueError(f"Invalid operator: {op}")
        
        # Reverse the operand list to maintain left-to-right evaluation
        operands.reverse()
        result = operands.pop(0)
        while operands:
            result = ops[op](result, operands.pop(0))
        stack.push(result)

    for token in tokens:
        if token == ')':
            compute()
        elif token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.push(int(token))
        elif token in ops:
            stack.push(token)
        elif token == '(':
            pass  # Ignore '('
        else:
            raise ValueError(f"Invalid token: {token}")

    return stack.pop() if not stack.is_empty() else None

if __name__ == "__main__":
    while True:
        try:
            expression = input("Enter an expression (or type 'exit' to quit): ")
            if expression.lower() == 'exit':
                break
            result = evaluate_expression(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)