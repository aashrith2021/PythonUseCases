# This is a simple calculator program

#function for calculating sum of two numbers
def Addition(num_1,num_2):
    return num_1 + num_2

#function for calculating difference of two numbers
def Subtraction(num_1,num_2): return num_1-num_2

#function for calculating product of two numbers
def Multiplication(num_1,num_2): return num_1*num_2

#function for calculating division of two numbers
def Division(num_1,num_2): return num_1/num_2

#Taking user option and inouts for performing operation
Operation_to_perform=int(input("""
        Select the operation to perform 
        1.Addition
        2.Subtraction
        3.Multiplication
        4.Division
        """))

num_1=int(input("Enter the first number"))
num_2=int(input("Enter the second number"))

#mapping option to related operation

if Operation_to_perform==1:
    print(num_1, " + ", num_2, " = ", Addition(num_1,num_2))

elif Operation_to_perform==2:
    print(num_1, " - ", num_2, " = ", Subtraction(num_1,num_2))

elif Operation_to_perform==3:
    print(num_1, " * ", num_2, " = ", Multiplication(num_1,num_2))

elif Operation_to_perform==4:
    print(num_1, " / ", num_2, " = ", int(Division(num_1,num_2)))

else:
    print("Invalid Input")




