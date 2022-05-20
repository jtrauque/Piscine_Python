
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
        if isinstance(account, Account):
            self.account.append(account)

    def transfer(self, origin, dest, amount):
        o = self.find_account(origin)
        d = self.find_account(dest)
        if o is None or d is None:
            print("Accounts origin or dest not found")
            return False
        if self.check_corruption(o) != 0 or self.check_corruption(d) != 0:
            print("======> Account(s) Corrupted !")
            return False
        if amount < 0 or amount > o.value or\
           not isinstance(amount, (float, int)):
            print("Error amount")
            return False
        d.transfer(amount)
        o.transfer(-amount)
        print(f"{o.name} gives {amount} to {d.name}")
        print(f"Transfer completed - origin value :\
             {o.value} and dest value : {d.value}")
        return True

    def find_account(self, account):
        if isinstance(account, int) and not None:
            for find in self.account:
                if account == find.id:
                    return find
            print("Account not found please provide us the name or the ID")
            return False
        elif isinstance(account, str) and not None:
            for find in self.account:
                if account == find.name:
                    return find
            print(f"Account {account} not found please provide us the name/ID")
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
                print(f"{account.name} corrupted: b detected")
                return 4
            num += 1
        print("NUM = ", num)
        if char is False:
            print(f"{account.name} corrupted: zip or addr missing")
            return 1
        if not all(hasattr(account, attr) for attr in ['name', 'id', 'value']):
            print(f"{account.name} corrupted: attribute(s) missing")
            return 3
        if num % 2 == 0:
            print(f"{account.name} corrupted: Even number of attibutes")
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
                    setattr(find, '_' + i[1:], getattr(find, i))
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

print("-------------CORRECTION--------------")

bank = Bank()
john = Account(
    'John',
    zip='100-064',
    brother="heyhey",
    value=6460.0,
    ref='58ba2b9954cd278eda8a84147ca73c87',
    info=None,
    other='This is the vice president of the corporation',
    lol="hihi"
)

jane = Account(
   'Jane',
   zip='100-064',
   rother="heyhey",
   value=6460.0,
   ref='58ba2b9954cd278eda8a84147ca73c87',
   info=None,
   other='This is the vice president of the corporation',
)

julie = Account(
   'Julie',
   zip='100-064',
   rother="heyhey",
   ref='58ba2b9954cd278eda8a84147ca73c87',
   info=None,
   other='This is the vice president of the corporation',
)

bank.add(john)
bank.add(jane)
bank.add(julie)
bank.transfer("Jane", "John", 500)
bank.transfer("Julie", "Jane", 500)
print("+++++++++++++++FIX+++++++++++++++++")
bank.fix_account('Jane')
bank.fix_account('John')
bank.transfer("Jane", "John", 500)
bank.transfer("Jane", "John", 7000)
