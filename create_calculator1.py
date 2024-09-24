#TASK-3
#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create_calculator(x,y,sign):
    if sign=='+':
        c=x+y
    elif sign=='-':
        c=x-y
    elif sign=='*':
        c=x*y
    elif sign=='/':
        c=x/y
    else:
        print("Invalid sign")
    print("Result is:",c)
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
s=input("Enter the sign of your choice:")
create_calculator(a,b,s)
