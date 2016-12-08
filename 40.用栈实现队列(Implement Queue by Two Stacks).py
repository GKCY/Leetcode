'''
正如标题所述，你需要使用两个栈来实现队列的一些操作。

队列应支持push(element)，pop() 和 top()，其中pop是弹出队列中的第一个(最前面的)元素。

pop和top方法都应该返回第一个元素的值。
'''


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
      
    def adjust(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
                
    def push(self, element):
        # write your code here
        self.stack1.append(element)

    def top(self):
        # write your code here
        # return the top element
        self.adjust()
        return self.stack2[-1]
        
    def pop(self):
        # write your code here
        # pop and return the top element
        self.adjust()
        return self.stack2.pop()
