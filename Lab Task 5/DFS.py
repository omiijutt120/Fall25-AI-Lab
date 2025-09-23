tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

class Stack:
    def __init__(self):
        self.tree = []

    def push(self, x):
        self.tree.append(x)

    def pop(self):
        if self.tree:
            return self.tree.pop()
        return None

def dfs():
    v = []
    stack = Stack()
    stack.push('A')

    while stack.tree:
        n = stack.pop()
        if n not in v:
            v.append(n)
            for i in reversed(tree[n]):
                stack.push(i)
    return v

print(dfs())
