class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        if self.items:
            return self.items.pop()

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': [],
    'F': ['I', 'K'],
}

start = 'A'
goal = input("Enter your Goal : ").upper()

n_v = []
s = Stack()
s.push(start)

while s.items:
    a = s.pop()
    if a not in n_v:
        n_v.append(a)
        if a == goal:
            print("Output:", n_v)
            exit()
        for child in graph[a]:
            s.push(child)

print("Error")
