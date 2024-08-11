#python project on calculator
#addition
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("Please select the operation")
print("1.Addition")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#give operation
choice=int(input("Select the above operations from (1, 2, 3, 4 :)"))

number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
if choice==1:
    print(number1, "+", number2, "=", add(number1,number2))
elif choice==2:
    print(number1, "-", number2, "=", subtract(number1,number2))
elif choice==3:
    print(number1, "*", number2, "=", multiply(number1,number2))
elif choice==4:
    print(number1, "/", number2, "=", divide(number1,number2))
else:
    print("Invalid choice")