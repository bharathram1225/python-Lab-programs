while True:
	print("\n \n")
	print("1. Size in bytes:")
	print("2. Length")
	print("3. Add new value")
	print("4. pop ")
	print("5. Intersection")
	print("6. Set difference")
	print("7. Symmentric difference")
	print("8. Check for element in the set")
	print("9. Clearing a set")
	print("10. Deleting a set")

	print("\n \n")


	set1 = {1,2,3,4,5,6,7,8}
	set2 = {3,4,5,6,7,8}
	set3 = {'perl','python','java'}
	print(set1)
	print(set2)
	print(set3)

	choice= int(input("Enter the choice"))
	print("\n \n")


	if choice == 1:
		print("The size of the set1 is: ",set1.__sizeof__())
	elif choice == 2:
		print("Length of the set is: ",len(set1))
	elif choice == 3:
		n=input("Enter the number/string to add in the set ")
		print("After adding the new value",n,"to the set",set1.add(n))
		print(set1)
	elif choice == 4:
		print(set1)
		print("It pop the first element in the set",set1.pop())
		print(set1)
	elif choice == 5:
		print(set1)
		print(set2)
		print("intersetction of 2 sets",set1.intersection(set2))
	elif choice == 6:
		print("the difference between two sets are",set1-set2)
	elif choice == 7:
		print("The symmentric difference between 2 sets: ",set1^set2)
	elif choice == 8:
		print(set1)
		n=int(input("Enter the number/string to add in the set "))
		print("Check for an element in the set")
		a=set1.__contains__(n)
		print(a)

	elif choice == 9:
		print("Clearing a set",set1.clear())
	elif choice == 10:
		print("Deleted the set")
		del set1
	else:
		print("Invalid Input")

