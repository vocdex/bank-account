# Bank Account Simulations
"""
    BankAccount class is a class that simulates a bank account.
    Init: name,balance, pin
    Methods:
        deposit(amount,pin): deposit amount to the account
        withdraw(amount,pin): withdraw amount from the account
        check_balance(pin): check the balance of the account
        transfer(amount,pin,other_account): transfer amount from the account to other_account
        convert(amount,pin,currency): convert amount from the account to currency
        all_accounts(): return all accounts in the bank
    """
class BankAccount:
    currencyRates = {"USD":1,"YEN":1/132,"EUR":1.2,"GBP":1.4,"CNY":1.28}
    allAccounts=[]
    @classmethod
    def all_accounts(cls):
        for instance in BankAccount.allAccounts:
            print(instance)
        return None
    @classmethod
    def create_account(cls,name,balance,password):
        if name in cls.allAccounts:
            print("Account already exists")
            return None
        newAccount=BankAccount(name,balance,password)
        # BankAccount.name=name
        # BankAccount.password=password
        # BankAccount.balance=balance
        print("Account created successfully")
        return newAccount
    @classmethod
    def switch_account(cls,name,password):
        if password!=cls.password:
            print("Incorrect password")
            return None
        cls.name=name
        print("Account switched successfully")
    def __init__(self,name,balance,password):
        self.name=name
        self.balance=balance
        self.password=password
        self.__class__.allAccounts.append((self))

    def deposit(self,currency,amount,password):
        if password!=self.password:
            print("Incorrect password")
            return None
        if amount<0:
            print("Invalid amount")
            return None
        print("Deposit successful")
        self.balance+=amount
        return self.balance
    def withdraw(self,amountToWithdraw,password):
        if password!=self.password:
            print("Incorrect password")
            return None
        if amountToWithdraw>self.balance:
            print("Insufficient funds for withdrawal")
            return None
        print("Withdrawal successful")
        self.balance-=amountToWithdraw
        return self.balance
    def check_balance(self,password):
        if password==self.password:
            return self.name+"'s current balance: "+str(self.balance)
        else:
            print("Incorrect password")
            return None
    def transfer(self,amount,password,otherAccount):
        if password!=self.password:
            print("Incorrect password")
            return None
        if amount>self.balance:
            print("Insufficient funds for transfer")
            return None
        if amount<0:
            print("Invalid amount")
            return None
        if otherAccount not in self.allAccounts:
            otherAccount=BankAccount(otherAccount,0,0)
        otherAccount.deposit(amount,otherAccount.password)
        self.withdraw(amount,self.password)
        print("Transfer successful")
    def convert(self,amount,password,original_currency,desired_currency):
        #Converts the given amount from the original currency to a desired currency.
        if password!=self.password:
            print("Incorrect password")
            return None
        if amount<0:
            print("Invalid amount.Please enter a positive amount")
            return None
        if self.balance<amount:
            print("Insufficient funds for conversion.Please deposit more money first")
            return None
        if original_currency not in self.currencyRates:
            print("Invalid currency")
            return None
        if desired_currency not in self.currencyRates:
            print("Invalid currency")
            return None
        if original_currency==desired_currency:
            print("No conversion necessary")
            return None
        converted_amount=amount*self.currencyRates[original_currency]/self.currencyRates[desired_currency]
        original_currency_balance=self.balance-amount
        desired_currency_balance = (self.balance - amount) * self.currencyRates[original_currency] / \
                                   self.currencyRates[desired_currency]
        desired_currency_balance=desired_currency_balance if original_currency_balance!=0 else self.balance*self.currencyRates[original_currency]/self.currencyRates[desired_currency]

        print(f"Conversion successful! \n Original currency balance: {original_currency} {original_currency_balance:.3f} \n Desired currency balance: {desired_currency} {desired_currency_balance:.3f}")
        return converted_amount
    def __str__(self):
        return "Account name: "+self.name+"\nAccount password: "+str(self.password)+"\nAccount current balance: "+str(self.balance)
def main():
    print("Welcome to the bank!")
    name=input("Enter your name: ")
    balance=float(input("Enter your initial balance: "))
    password=input("Enter your password: ")
    account=BankAccount(name,balance,password)
    print("Account created successfully")
    print("Your account details:")
    print(account)
    print("\n")
    print("Please select an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Transfer")
    print("5. Convert")
    print("6. All accounts")
    print("7. Create new account")
    print("8. Switch account")
    print("9. Exit")

    while True:
        option=int(input("Enter your option: "))
        if option==1:
            amount=float(input("Enter the amount to deposit: "))
            password=input("Enter your password: ")
            account.deposit(amount,password)
            print("\n")
            print("Please select an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Transfer")
            print("5. Convert")
            print("6. All accounts")
            print("7. Create new account")
            print("8. Switch account")
            print("9. Exit")
        elif option==2:
            amount=float(input("Enter the amount to withdraw: "))
            password=input("Enter your password: ")
            account.withdraw(amount,password)
            print("\n")
            print("Please select an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Transfer")
            print("5. Convert")
            print("6. All accounts")
            print("7. Create new account")
            print("8. Switch account")
            print("9. Exit")
        elif option==3:
            password=input("Enter your password: ")
            print(account.check_balance(password))
            print("\n")
            print("Please select an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Transfer")
            print("5. Convert")
            print("6. All accounts")
            print("7. Create new account")
            print("8. Switch account")
            print("9. Exit")
        elif option==4:
            amount=float(input("Enter the amount to transfer: "))
            password=input("Enter your password: ")
            otherAccount=input("Enter the name of the account to transfer to: ")
            account.transfer(amount,password,otherAccount)
            print("\n")
            print("Please select an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Transfer")
            print("5. Convert")
            print("6. All accounts")
            print("7. Create new account")
            print("8. Switch account")
            print("9. Exit")
        elif option==5:
            amount=float(input("Enter the amount to convert: "))
            password=input("Enter your password: ")
            original_currency=input("Enter the original currency: ")
            desired_currency=input("Enter the desired currency: ")
            account.convert(amount,password,original_currency,desired_currency)
            print("\n")
            print("Please select an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Transfer")
            print("5. Convert")
            print("6. All accounts")
            print("7. Create new account")
            print("8. Switch account")
            print("9. Exit")
        elif option==6:
            print("All accounts:")
            for account in BankAccount.allAccounts:
                print(account)
            print("\n")
            print("Please select an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Transfer")
            print("5. Convert")
            print("6. All accounts")
            print("7. Create new account")
            print("8. Switch account")
            print("9. Exit")
        elif option==7:
            new_name=input("Enter the name of the new account: ")
            new_balance=float(input("Enter the initial balance: "))
            new_password=input("Enter the password: ")
            newAccount=BankAccount.create_account(new_name,new_balance,new_password)
            print("New account details:")
            print(newAccount)
            print("\n")
            print("Please select an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Transfer")
            print("5. Convert")
            print("6. All accounts")
            print("7. Create new account")
            print("8. Switch account")
            print("9. Exit")
        elif option==8:
            name=input("Enter the name of the account to switch to: ")
            password=input("Enter the password: ")
            account=BankAccount.switch_account(name,password)
            print("\n")
            print("Please select an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Transfer")
            print("5. Convert")
            print("6. All accounts")
            print("7. Create new account")
            print("8. Switch account")
            print("9. Exit")
        elif option==9:
            print("Thank you for using the bank!")
            break
        else:
            print("Invalid option")
            print("\n")
            print("Please select an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Transfer")
            print("5. Convert")
            print("6. All accounts")
            print("7. Create new account")
            print("8. Switch account")
            print("9. Exit")
if __name__ == '__main__':
    main()