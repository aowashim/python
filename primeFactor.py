no = int(input("Enter your number : "))
no1 = no
lst = []
while no % 2 == 0:
	lst.append(2)
	no //= 2
for i in range(3,no//2,2):
	while no % i == 0:
		lst.append(i)
		no //= i
if no != 1:
	lst.append(no)
print(f"The primme factors of {no1} are : {lst}")