stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print('The Stack is :',stack)
print('Pop the element :',stack.pop())
print('After Pop the stack is :',stack)
print('Pop the element :',stack.pop())
print('Pop the element :',stack.pop())
print('After Pop the stack is :',stack)
stack.append(10)
print('Push the element 10')
print('After Push the stack is :',stack)

'''
OUTPUT
------
The Stack is : [3, 4, 5, 6, 7]
Pop the element : 7
After Pop the stack is : [3, 4, 5, 6]
Pop the element : 6
Pop the element : 5
After Pop the stack is : [3, 4]
Push the element 10
After Push the stack is : [3, 4, 10]
'''