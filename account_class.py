class Account:

	def __init__(self,owner,balance):
		self.owner = owner
		self.balance = balance

	def deposit(self,d_amount):
		self.balance += d_amount
		print(f"{d_amount} deposited")

	def withdraw(self,w_amount):
		if w_amount <= self.balance:
			self.balance -= w_amount
			print(f"{w_amount} withdrawn.")
		else:
			print(f"{w_amount} is not available.")

cs1 = Account('Ramen',300)
print(cs1.owner)
print(cs1.balance)
cs1.withdraw(100)
cs1.withdraw(250)
cs1.deposit(100)
cs1.withdraw(250)
print(cs1.balance)