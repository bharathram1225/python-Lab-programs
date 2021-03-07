from calculation import *

while True:
    print("1. overload + operator")
    print("2. overload - operator")
    print("3. overload * operator")
    print("4. overload // operator")
    print("5. Exit")
    
    ch = int(input("Enter the your choice: "))

    if ch ==1:
        op1=Operation()
        op2=Operation()
        op1.accept()
        op2.accept()
        print(op1+op2)
    elif ch==2:
        print(op1-op2)
    elif ch==3:
        print(op1*op2)
    elif ch==4:
        print(op1//op2)
    elif ch==5:
        break

    else:
        print("Invalid choice: ")
        break
