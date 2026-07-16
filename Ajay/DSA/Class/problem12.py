class BankAccount: # Creating a class Object of BankAccount
    def __init__(self, account_name, balance): #Definfing Object
        self.name = account_name #1st Object Name of Account Holder
        self.balance = balance # 2nd Object Balance of Account Holder

    def deposit(self, amount): # Creating a Deposite Function to Deposite Ammount in the Account
        self.balance = self.balance + amount
        print(f'''
            
            Deposite balance     -> {amount}
            Total Balance Now    -> {self.balance}''')

b1 = BankAccount("Ajay", 1000) # Assigning Values to the objects By Creating an init function
b1.deposit(500) # Giving an Amount to Deposite into Account
b1.deposit(500) # Giving an Amount to Deposite into Account
