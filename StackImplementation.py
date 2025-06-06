class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
          return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    def is_empty(self):
         return len(self.items)==0
    def size(self):
        return len(self.items)

if __name__=="__main__":
   stack = Stack()
   stack.push(10)
   stack.push(13)
   stack.push(40)
   print("Need to Peek for:",stack.peek())
   print("Len of the Stack is:",stack.size())
   print("After popping from stack, we got:",stack.pop())
   print("What is the  current size? Ans:",stack.size())
   print("Peeking into it, we find:",stack.peek())
   print("Stack Size after Peeking into it",stack.size())
