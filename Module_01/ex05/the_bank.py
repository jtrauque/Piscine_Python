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
		o = find_account(origin)
		d = find_account(dest)
		if o == -1 or d == -1:
			print("Accounts origin or dest not found")
			return False
		if (self.account[]
		
	def find_account(self, account):
		if isinstance(account, int):
			for i in self.account:
				if account == self.account.id:
					return i
			return False
		elif isinstance(account, str):
			for i in self.account:
				if account == self.account.name:
					return i
		else:
			print("Account not found please provide us the name or the ID")
			return -1

	def fix_account(self, account):
		
