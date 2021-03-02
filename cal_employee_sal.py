d ={}
class Employee:
    def salary_slip(self,name,address,panno,basic,tds=0,deduct=0):
        self.name=name
        self.address=address
        self.panno=panno
        self.basic=basic
        self.hra=basic*1.175
        self.cca=300
        self.pf=1300
        self.pt=200
        self.tds=tds
        self.deduct=deduct
        self.da=0.25*basic
        netsal = self.basic+self.da+self.hra+self.cca-(self.pf+self.pt+self.tds+self.deduct)
        return netsal
    
    def accept(self):
        name = input("Enter the name: ")
        address = input("Enter the address: ")
        panno = input("Enter the panno: ")
        basic = int(input("Enter the basic: "))
        tds = int(input("Enter the tds: "))
        deduct = int(input("Enter the deduct: "))
        self.netsal = self.salary_slip(name,address,panno,basic,tds,deduct)

    def display(self):
        print("name: ",self.name)
        print("address: ",self.address)
        print("panno: ",self.panno)
        print("basic: ",self.basic)
        print("hra: ",self.hra)
        print("da: ",self.da)
        print("cca: ",self.cca)
        print("pf: ",self.pf)
        print("pt: ",self.pt)
        print("tds: ",self.tds)
        print("deduct: ",self.deduct)
        print("netsal: ",self.netsal)


    def search(self,name):
        for k,v in d.items():
            print("Key ==",k)
            print("Value ==",v)
            if k==name:
                print("name:{0}, address:{1}, panno:{2}".format(v.name,v.address,v.panno))
                print("basic:{0}, hra:{1}, da:{2}, cca:{3}, pf:{4}, pt:{5}, tds:{6}, deduct:{7}, netsalary:{8}".format(v.basic,v.hra,v.da,v.cca,v.pf,v.pt,v.tds,v.deduct,v.netsal))
                
    




while True:
    print("*"*20)
    print("1 . Enter the employee details: ")
    print("2 . Display the details: ")
    print("3 . Update the details to the dictionary: ")
    print("4 . Search for the details: ")
    print("5 . quit: ")
    ch = int(input("Enter the choice: "))
    if ch ==1:
        e1=Employee()
        print(id(e1))
        e1.accept()
    elif ch==2:
        e1.display()
    elif ch==3:
        d.update({e1.name:e1})
    elif ch==4:
        print("Search the name in dict: ")
        e1.search(input("Enter the name"))
    elif ch==5:
        break
    else:
        print("Please enter the valid input;")
    
                      
                        

        
