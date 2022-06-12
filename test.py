import unittest
from bank_account.account_class import BankAccount
class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account=BankAccount("John",100,"123")
        self.assertEqual(account.deposit(100,"123",True),200)
    def test_withdraw(self):
        account=BankAccount("John",100,"123")
        self.assertEqual(account.withdraw(50,"123",True),50)
    def test_check_balance(self):
        account=BankAccount("John",100,'123')
        self.assertEqual(account.check_balance('123'),"John's current balance: 100")
    def test_convert(self):
        account=BankAccount("John",100,'123')
        self.assertEqual(account.convert(100,'123','USD','YEN'),13200.0)
    def test_transfer(self):
        account1=BankAccount("John",100,'123')
        account2=BankAccount("Jane",100,'123')
        self.assertEqual(account1.transfer(50,'123',account2),150)
        self.assertEqual(account2.balance,150)
if __name__=="__main__":
    unittest.main()
