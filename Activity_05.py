input_line = input("Enter 5 numbers:-\n")
numbers = input_line.split(' ')
list=[numbers]
sum = 0
for i in numbers:
	sum = sum + int(i)
print("Sum of all numbers is",sum)
