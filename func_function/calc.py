from func_function.divide import divide
from func_function.multiply import multiply
from func_function.subtruction import subtruction
from func_function.sum import sum
from func_function.ask_operation import ask_operation
# from func_function.square import pow
def calculate (num1, num2, operation):
     result = None

     if operation =='+':
          result= sum(num1, num2)
     elif operation =='-':
          result = subtruction(num1, num2)
     elif operation =='*':
          result = multiply(num1, num2)
     elif operation == '/':
          if num2 =='0':
              print("Error! Can't divide by zero")
          else:
              result = divide(num1, num2)
     elif operation =='**':
          num1=input("Enter number1: ")
          result=pow(num1)
     
          
     return result
    
   