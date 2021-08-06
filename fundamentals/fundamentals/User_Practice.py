
class User:

    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit (self, amount):
        self.account_balance += amount

    def make_withdrawal (self, amount):
        self.account_balance -= amount

    def display_user_balance (self):
        print(self.account_balance)

    # def transfer_money (self, recipient, amount):
    #     if amount > 0:
    #         [recipient].make_deposit(self, amount)
    #     if amount < 0:
    #         [recipient].make_withdrawal(self,amount)

jim = User("Jim Kirk", "starfleet79@gmail.com")
spock = User("Just Spock", "Vulcan@gmail.com")
bones = User("Leonard McCoy", "DammitJim@gmail.com")


spock.make_deposit(100)
spock.make_deposit(200)
spock.make_deposit(75)
spock.make_withdrawal(85)
spock.display_user_balance()

bones.make_deposit(50)
bones.make_deposit(85)
bones.make_withdrawal(60)
bones.make_withdrawal(30)
bones.display_user_balance()

jim.make_deposit(500)
jim.make_withdrawal(50)
jim.make_withdrawal(100)
jim.make_withdrawal(30)
jim.display_user_balance()

# jim.transfer_money("bones",300)

