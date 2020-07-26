def find_prime(no):
	if no == 2 or no == 3:
		return True
	elif no % 2 == 0:
		return False
	for i in range(3,no//2,2):
		if no % i == 0:
			return False
	return True			

print(f"The first prime no. is : {2}.")
ch = 'y'
n_no = 3
while ch == 'y' or ch == 'Y':
	while True:
		if find_prime(n_no):
			print(f"The next prime no. is : {n_no}.")
			n_no += 2
			break
		n_no += 2
	print("Press 'y' for next prime and press 'n' to quit.")
	ch = input("Enter your choice 'y' or 'n' : ")

