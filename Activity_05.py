input_line = input("Enter 5 numbers:-\n")
numbers = input_line.split(' ')
list=[numbers]
print(list)
sum = 0
for i in numbers:
	sum = sum + int(i)
print(sum)
