while True:
	print("\n \n")
	print("1. repetition")
	print("2. Concatination")
	print("3. Reversing")
	print("4. Range slicing")
	print("5. Slicing")
	print("6. String membership")
	print("7. Iterating though string")
	print("8. Couting number of occurance")
	print("9. Capitalize")
	print("10. Spliting")
	print("\n \n")
	choice= int(input("Enter the choice"))
	print("\n \n")

	if choice == 1:
		val1=input("enter the first string :")
		n=int(input("Enter the number of times need to be repeated :"))
		print("the",val1,"is repeated",n,"times \nthe results are",val1*n)
	elif choice == 2:
		val1=input("enter the first string :")
		val2=input("enter the second string :")
		print("Concatination of 2 strings are",val1+val2)
		print("\n \n")
	elif choice == 3:
		val1=input("enter the String :")
		print("The reversed string is",val1[::-1])
	elif choice == 4:
		val1=input("enter the String :")
		n=int(input("enter the staring interger value to get the substring: "))
		m=int(input("enter the end interger value to get the substring: "))
		print("the substring of the above string is",val1[n:m])
		print("\n \n")
	elif choice == 5:
		val1=input("enter the String :")
		n=int(input("enter the interger value to get the substring: "))
		print("the substring of the above string is",val1[n])
		print("\n \n")

	elif choice == 6:
		val1=input("enter the String :")
		a=input("Provide the character or the string to check whether it is present")
		print(a in val1)
	elif choice == 7:
		val1=input("enter the String :")
		print("find the each charaters: ")
		for i in val1:
			print(i,end=" ")
	elif choice == 8:
		val1=input("enter the String :")
		a = input("enter the single charater and check how many times it is been iterated: ")[0]
		print("Count number of occurances in the string",val1.count(a))
		print("\n \n")

	elif choice == 9:
		val1=input("Enter the string: ")
		print("Check the capitalized string: ",val1.upper())

	elif choice == 10:
		val1=input("Enter the string: ")
		print("splited string",val1.split())
	else:
		print("Invalid Input")
