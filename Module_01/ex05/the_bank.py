class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		Account.ID_COUNT += 1
	def transfer(self, amount):
		self.value += amount

class Bank:
	def __init__(self, accounts):
		self.account = []

	def add(self, account):
		self.account.append(account)

	def transfer(self, origin, dest, amount):
		o = self.find_account(origin)
		d = self.find_account(dest)
		if o == None or d == None:
			print("Accounts origin or dest not found")
			return False
		print(f"{o.name} gives {amount} to {d.name}")
		if amount < 0 or amount > o.value or not isinstance(amount, (float, int)):
			print("Error amount")
			return False
		d.tranfert(amount)
		o.value -= amount
		return True
		
	def find_account(self, account):
		if isinstance(account, int) and not None:
			print("INT")
			for find in self.account:
				if account == find.account.id:
					return find
			return False
		elif isinstance(account, str) and not None:
			print("STR")
			for find in self.account:
				if account == find.account.name:
					return find
			return False
		else:
			print("Account not found please provide us the name or the ID")
			return -1

#	def fix_account(self, account):	

a1 = Account("Tom")	
a2 = Account("Bob")
B = Bank
B.add(a1)
B.add("Bob")
B.transfer("Tom", "Bob", 20)