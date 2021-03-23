class Student:
	def __init__(self,usn,name,age):
		self.usn = usn
		self.name = name
		self.age = age
		
	def getdata(self):
		self.usn = int(input("Enter the USN:"))
		self.name = input("Enter the Name:")
		self.age = int(input("Enter the Age:"))
	
	def displaystu(self):
		print("The student name is ",self.name," with an age ",self.age," also has usn",self.usn);

class pgstudent(Student):
	def __init__(self,sem = 0 ,fees = 0,stipend = 0):
		self.sem = sem
		self.fees = fees
		self.stipend = stipend
	
	def pggetdata(self):
		self.sem = int(input("Enter the sem:"))
		self.fees = int(input("Enter the fees:"))
		self.stipend = int(input("Enter the stipend:"))
	
	def display(self):
		print("The student sem is ",self.sem," with an fees ",self.fees," also has stipend",self.stipend);
	
		
class ugstudent(Student):
	def __init__(self,sem = 0,fees = 0,stipend = 0):
		self.sem = sem
		self.fees = fees
		self.stipend = stipend
	
	def uggetdata(self):
		self.sem = int(input("Enter the sem:"))
		self.fees = int(input("Enter the fees:"))
		self.stipend = int(input("Enter the stipend:"))
	
	def display(self):
		print("The UG student sem is ",self.sem," with an fees ",self.fees," also has stipend",self.stipend);
		

pg = pgstudent()
pg.pggetdata()
pg.display()
ug = ugstudent()
ug.uggetdata()
ug.display()
pg.getdata()
pg.displaystu()
