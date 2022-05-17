
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
	def __init__(self):
		self.account = []

	def add(self, account):
		self.account.append(account)

	def transfer(self, origin, dest, amount):
		o = self.find_account(origin)
		d = self.find_account(dest)
		if o == None or d == None :
			print("Accounts origin or dest not found")
			return False
		if self.check_corruption(o) != 0 or self.check_corruption(d) != 0:
			print("Account(s) Corrupted !")
			return False
		if amount < 0 or amount > o.value or not isinstance(amount, (float, int)):
			print("Error amount")
			return False
		d.transfer(amount)
		o.transfer(-amount)
		print(f"{o.name} gives {amount} to {d.name}")
		print(f"Transfer completed - origin value : {o.value} and dest value : {d.value}")
		return True
		
	def find_account(self, account):
		if isinstance(account, int) and not None:
			for find in self.account:
				if account == find.id:
					return find
			return False
		elif isinstance(account, str) and not None:
			for find in self.account:
				if account == find.name:
					return find
			return False
		else:
			print("Account not found please provide us the name or the ID")
			return False

	def check_corruption(self, account):
		num = 0
		char = False
		print("Check_corr")
		for i in account.__dict__:
			print("--> ", i)
			if i.find("zip") != -1 or i.find("addr") != -1:
				char = True
			if i[0] == 'b':
				return 4	
			num += 1
		print("NUM = ", num)
		if char == False:
			return 1
		if not all(hasattr(account, attr) for attr in ['name', 'id', 'value']):
			return 3
		if num % 2 == 0:
			return 2
		return 0

	def fix_account(self, account):
		print("Fix account")
		find = self.find_account(account)
		if not find:
			return False	
		ret = self.check_corruption(find)
		if ret == 0:
			print("Fixed account")
			return True
		if ret == 1:
			setattr(find, 'zipcode', 92270)
		elif ret == 2:
			setattr(find, 'odd', 0)
		elif ret == 3:
			if not hasattr(find, 'value'):
				setattr(find, 'value', 0)
			if not hasattr(find, 'name'):
				find.name = 'default'
			if not hasattr(find, 'id'):
				find.id = Account.ID_COUNT
		else:
			for i in find.__dict__:
				if i[0] == 'b':
					setattr(find, '_'+ i[1:], getattr(find, i))
					delattr(find, i)
					break 
		return self.fix_account(find.name)

		

a1 = Account('Tom')	
a2 = Account('Bob')
B = Bank()
B.add(a1)
B.add(a2)
print("-----------Account created------------")
B.transfer(1, 'Bob', 20)
print("----------Transfert abort------------")
B.fix_account('Tom')
B.fix_account(2)
print("--------------Account checked and fixed----------------")
a1.transfer(50)
B.transfer('Tom', 'Bob', 20)
