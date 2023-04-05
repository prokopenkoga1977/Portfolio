# 1) Calculator -> + , * , / , -
# 2) square
# 3) Error handling : try , except , finally


from func_function.calc import calculate
from func_function.ask_operation import ask_operation
from func_function.square import pow

is_running=True

while is_running :
    user_choose = input("Do you want to work with calc? y/n : ")

    if user_choose == "y":
        operation=ask_operation()
        if operation =='**':
            num1=int(input("Enter number1: "))
            result=pow(num1)
            print(result)
        else:
            try:
                   num1 = int(input("Enter number1: "))
                   num2 = int(input("Enter number2: "))
                   result=calculate (num1, num2, operation)
                   print(result)
            except ValueError:
                  print("Enter only numbers")
            except ZeroDivisionError:
                  print("Division by zero")
            finally:
                 print("Success")
             
    elif user_choose == "n":
        is_running = False
    else :
        continue