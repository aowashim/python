bi_no = int(input("Enter your number : "))
sbi_no = bi_no
deci_eq = 0
m = 0
while bi_no != 0:
	rem = bi_no % 10
	deci_eq += rem*2**m
	bi_no //= 10
	m += 1

bi_eq = 0
m = 0
deci_no = deci_eq
while deci_no != 0:
	rem = deci_no % 2
	bi_eq += rem*10**m
	deci_no //= 2
	m += 1

print(f"The decimal equivalent of {sbi_no} is = {deci_eq}.")
print(f"The binary equivalent of {deci_eq} is = {bi_eq}.")