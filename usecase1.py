#example for operations that can be performed on a python list

#declaring a list
names_of_employees=['Prasanth','Charan','Chani','Srekar']

#looping the user operations
while(True):
    option = int(input("""
        Enter your choice key
        1.Add Employee
        2.Print Employee
        3.remove employee
        4.Exit
        """))

    # Adding elements to the list from user input by appending it to the list
    if option == 1:
        new_employee = input('Enter the new employee name')
        names_of_employees.append(new_employee)

    #printing elements from the list of names
    elif option == 2:
        for name in names_of_employees:
            print(name)

    #deleting the employee
    elif option == 3:
        delete_employee=input('Enter the name of the employee to remove from the list')
        if delete_employee in names_of_employees:
            names_of_employees.remove(delete_employee)
        else:
            print('Employee not found')

    #exit loop
    elif option == 4:
        break
