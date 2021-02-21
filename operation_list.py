print("lets creat 2 list")
print("list1: ")
number1= int(input("enter the number of element in the first list: "))
list1 = []
for i in range(number1):
	element = input("Enter the elements: ")
	list1.append(element)


print("list2: ")
number2= int(input("enter the number of element in the second list: "))
list2 = []
for i in range(number2):
	element = input("Enter the elements: ")
	list2.append(element)

for i in range(3):
	print(" "*3)

print(list1)
print()
print()
print(list2)

for i in range(3):
	print(" "*3)




while True:
	print("1. Creating an Empty List1: ")
	print("2. Adding element to the List1: ")
	print("3. concatination of List1: ")
	print("4. Repitation of the List1: ")
	print("5. Range slicing: ")
	print("6. Iteration through the List1")
	print("7. Length of the List1")
	print("8. pop the element the list1")
	print("9. Insert the element in the specified position: ")
	print("10. del the list1")
	choice = int(input("Enter the choice: "))
	for i in range(3):
		print(" "*3)
	if choice == 1:
		list3 = []
		print("The empty list is create",list3)
		for i in range(3):
			print(" "*3)
	elif  choice == 3:
		print("list 1",list1)
		print("list 2",list2)
		print("concatination of list",list1+list2)
		for i in range(3):
			print(" "*3)
	elif choice == 2:
		ele = input("Enter the element to append: ")
		list1.append(ele)
		print(list1)
		for i in range(3):
			print(" "*3)
	elif choice ==4:
		number = int(input("Enter the number of time to be repeated: "))
		print("the",list1,"is repeated",number,"times: ",list1*number)
		for i in range(3):
			print(" "*3)
	elif choice == 5:
		n = int(input("enter the initial range: "))
		m = int(input("enter the final range: "))
		print("the list is sliced from",n,"to",m,"in",list1,": ",list1[n:m])
		for i in range(3):
			print(" "*3)
	elif choice == 6:
		print("the list1 is  iterated: ",[i for i in list1])
		for i in range(3):
			print(" "*3)
	elif choice ==7:
		print("length of List1 is: ",len(list1))
		for i in range(3):
			print(" "*3)
	elif choice == 8:
		print("this is the list1",list1)
		print("the last item is poped out",list1.pop())
		print("After poping the element",list1)
		for i in range(3):
			print(" "*3)
	elif choice == 9:
		print(list1)
		pos = int(input("Enter the position to the element  to be added: "))
		item = input("Enter the element to be added: ")
		list1.insert(pos,item)
		print("The element is been added and the list1",list1)
		for i in range(3):
			print(" "*3)
	elif choice == 10:
		print("this list going to be deleted :")
		del list1
		print("the list is been deleted")
		for i in range(3):
			print(" "*3)
	else:
		print("invalid input, try again!!!!")
		break

