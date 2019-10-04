class Stack:
    def __init__(self,stack=[]):
        self.stack = []
        for i in stack:
            self.push(i)
    def isEmpty(self):
        return not self.stack
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if self.isEmpty():
            print("警告，栈为空")
        else:
            return self.stack.pop()
    def top(self):
        if self.isEmpty():
            print("警告，栈为空")
        else:
            return self.stack[-1]
    def bottom(self):
        if self.isEmpty():
            print("警告，栈为空")
        else:
            return self.stack[0]


if __name__ == '__main__':
    p = Stack()
    p.push(1)
    p.push(2)
    p.push(3)
    print("底部元数为: ",p.bottom())
    print("顶部元数为: ",p.top())
    print("出栈元数为: ",p.pop())
