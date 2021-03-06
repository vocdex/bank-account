# Bank Account Simulations
from bank_account.account_class import BankAccount
def command_line_input():
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


def main():
    print("Welcome to the bank!")
    name=input("Enter your name: ")
    balance=float(input("Enter your initial balance: "))
    password=input("Enter your password: ")
    account=BankAccount(name,balance,password)
    print("Account created successfully")
    print("Your account details:")
    print(account)
    command_line_input()
    while True:
        option=int(input("Enter your option: "))
        if option==1:
            amount=float(input("Enter the amount to deposit: "))
            password=input("Enter your password: ")
            account.deposit(amount,password)
            command_line_input()
        elif option==2:
            amount=float(input("Enter the amount to withdraw: "))
            password=input("Enter your password: ")
            account.withdraw(amount,password)
            command_line_input()
        elif option==3:
            password=input("Enter your password: ")
            print(account.check_balance(password))
            command_line_input()

        elif option==4:
            amount=float(input("Enter the amount to transfer: "))
            password=input("Enter your password: ")
            otherAccount=input("Enter the name of the account to transfer to: ")
            account.transfer(amount,password,otherAccount)
            command_line_input()
        elif option==5:
            amount=float(input("Enter the amount to convert: "))
            password=input("Enter your password: ")
            original_currency=input("Enter the original currency: ")
            desired_currency=input("Enter the desired currency: ")
            account.convert(amount,password,original_currency,desired_currency)
            command_line_input()
        elif option==6:
            print("All accounts:")
            for account in BankAccount.allAccounts:
                print(account)
            command_line_input()
        elif option==7:
            new_name=input("Enter the name of the new account: ")
            new_balance=float(input("Enter the initial balance: "))
            new_password=input("Enter the password: ")
            newAccount=BankAccount.create_account(new_name,new_balance,new_password)
            print("New account details:")
            print(newAccount)
            command_line_input()
        elif option==8:
            name=input("Enter the name of the account to switch to: ")
            password=input("Enter the password: ")
            account=BankAccount.switch_account(name,password)
            command_line_input()
        elif option==9:
            print("Thank you for using the bank!")
            break
        else:
            print("Invalid option")
            command_line_input()
if __name__ == '__main__':
    main()