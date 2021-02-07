while True:
	print("\n \n")
	print("1. Creation of tuple")
	print("2. Concatination")
	print("3. Repitation")
	print("4. Range slicing")
	print("5. Slicing")
	print("6. String membership")
	print("7. Iterating though string")
	print("8. Length of tuple")
	print("9. Maximum vvalue of tuple")
	print("10. Delete a tuple")
	print("\n \n")


	tuple1 = ('a','b','c','d','e')
	tuple2 = (3,4,'RVCE')
	tuple3 = (4,)
	print(tuple1)
	print(tuple2)
	print(tuple3)

	choice= int(input("Enter the choice"))
	print("\n \n")


	if choice == 1:
		print("this created an empty tuple: ")
		tuple4=()
		print(tuple4)
	elif choice == 2:
		print("concatination of 2 tuples are",tuple1+tuple2)
	elif choice == 3:
		n=int(input("Enter the number of times the tuple needs to be inputed: "))
		print("the tuple is been repeated",n,"times",tuple1*n)
	elif choice == 4:
		n=int(input("enter the staring interger value to get the substring: "))
		m=int(input("enter the end interger value to get the substring: "))
		print("the substring of the above string is",tuple1[n:m])
	elif choice == 5:
		n=int(input("enter the interger value to get the substring: "))
		print("the substring of the above string is",tuple1[n])
	elif choice == 6:
		a=input("Provide the element to check whether it is present in the tuple: ")
		print(a in tuple1)
	elif choice == 7:
		print("find the each element in the tuple: ")
		for i in tuple1:
			print(i,end=" ")
	elif choice == 8:
		a = input("The length of the tuple is: ")
		print("Count number of occurances in the string",len(tuple1))

	elif choice == 9:
		print("Check Maximun value from the tuple: ",max(tuple1))

	elif choice == 10:
		print("Deleted the tuple")
		del tuple1
	else:
		print("Invalid Input")

