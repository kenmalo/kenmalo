class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):

        print(user1.name, "has an account balance of :", self.balance)

    def withdrawal(self, Withdrawn):
        if self.balance > 0 and Withdrawn > 0:
           self.balance -= Withdrawn
        elif Withdrawn < 0:
            print("Withdrawn amount must be greater than 0")

    def deposit(self, Deposited):
        if Deposited > 0:
            self.balance += Deposited
        else:
            print("Deposited")

    def transfer_money(self, user1, Deposited):
        if Deposited < self.balance:
            print("You are transfering $", Deposited, 'to',  user1.name)
            print("Authentication is needed")

            if self.pin is True:
              print("transfer authorized")
              print("transferring $", float(Depoisted))

        else:
            print("Your pin is incorrect")
            return False


print(""" Driver Code for Task 1 """)

user1 = User("Bob", "1234", "password")
print(user1.name, user1.password, user1.pin)
user1.change_name("Bobby")
user1.change_pin(4321)
user1.change_password("newpassword")


print(user1.name, user1.password, user1.pin)
"""

""" Driver Code for Task 3"""

"""bankuser1 = BankUser("Bob", "1234", "password")
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)
"""

""" Driver Code for Task 4"""

bankuser1 = BankUser("Bob", "1234", "password")
bankuser1.show_balance()
bankuser1.deposit(1000)
bankuser1.show_balance()
bankuser1.withdrawal(100)
bankuser1.show_balance()
