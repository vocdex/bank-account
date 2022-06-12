import unittest
from bank_account.account_class import BankAccount
class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account=BankAccount("John",100,"123")
        self.assertEqual(account.deposit(100,"123"),200)
    def test_withdraw(self):
        account=BankAccount("John",100,"123")
        self.assertEqual(account.withdraw(50,"123"),50)
    def test_check_balance(self):
        account=BankAccount("John",100,'123')
        self.assertEqual(account.check_balance('123'),"John's current balance: 100")
    def test_transfer(self):
        account=BankAccount("John",100,'123')
        account2=BankAccount("Jane",100,'123')
        self.assertEqual(account.transfer(50,'123',account2),50)
        self.assertEqual(account2.balance,150)
if __name__=="__main__":
    unittest.main()
