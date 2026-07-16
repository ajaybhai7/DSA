class BankAccount:
    def __init__(self, ac_name, ac_balance):
        self.name = ac_name
        self.balance = ac_balance

    def deposit(self, amount): # Creating a Deposite Function to Deposite Ammount in the Account
        self.balance = self.balance + amount
        print(f'''
            
            Deposite balance     -> {amount}
            Total Balance Now    -> {self.balance}''')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f'''
            Withdraw Amount     -> {amount}
            Total Balance Now    -> {self.balance}''')

        else:
            print(f"Paise kam hai bhai! Aapka balance sirf {self.balance} hai, aur aap {amount} nikalna chate ho.")
        
b1 = BankAccount("Ajay", 1000)

b1.deposit(int(input("Enter Amount to Deposit: ")))
b1.withdraw(int(input("Enter Amount to Withdraw Money: ")))
