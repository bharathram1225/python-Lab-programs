class Student:
    def __init__(self,usn=None,name=None,age=None):
        self.usn=usn
        self.name=name
        self.age=age
	
    def getdata(self):
        self.usn = int(input("Enter the usn:"))
        self.name = input("Enter the name:")
        self.age = int(input("Enter the age:"))
        

class boy(Student):
    def __init__(self,sem=None,subject1=None,subject2=None,subject3=None,subject4=None,subject5=None):
        self.sem = sem
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.subject4 = subject4
        self.subject5 = subject5
        

    def subjectmarks(self):
        self.sem = int(input("enter the sem:"))
        self.subject1 = int(input("enter the subject1:"))
        self.subject2 = int(input("enter the subject2:"))
        self.subject3 = int(input("enter the subject3:"))
        self.subject4 = int(input("enter the subject4:"))
        self.subject5 = int(input("enter the subject5:"))

class girl(boy):

    def display(self):
        print("Subject1",self.subject1)
        print("Subject2",self.subject2)
        print("Subject3",self.subject3)
        print("Subject4",self.subject4)
        print("Subject5",self.subject5)
        
    def total(self):
        self.total = self.subject1+self.subject2+self.subject3+self.subject4+self.subject5
        print("the total marks",self.total)
        print("the Percentage",(self.total/5)*100)
        


g = girl(234,23456,2345,2345,23345)
g.subjectmarks()
g.display()
g.getdata()
g.total()


	
