class FunctionOverload:
    
    def hello(self,name=None,age=None):
        self.name = name
        self.age = age
        if name!=None and age!=None:
            print("my name is ",name,"and",age)
        elif self.age!=None:
            print(age)
        elif self.name!=None:
            print(name)
        else:
            print("The name and age value is empty")
            


while True:
    print("1. calling thw function with argument 1 argument")
    print("2. calling thw function with argument 2 argument")
    print("3. calling thw function with argument no argument")
    print("4. exit")
    choice = int(input("Enter your choice: "))
    c = FunctionOverload()
    if choice ==1:
        ch = input("Enter which value to read either the name or age ")
        if ch.isdigit()==True:
            c.hello(age=int(ch))
        else:
            c.hello(name=ch)
    elif choice ==2:
        name = input("Enther the name is:" )
        age = int(input("Enter the age of:" ))
        c.hello(name,age)
    elif choice ==3:
        print("Elements with no arguments")
        c.hello()
    elif choice ==4:
        break
        
                       
    

        
