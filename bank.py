from threading import activeCount


class Bankaccount:
      def __init__(self,account_name,balance,amount_withdraw,amount_deposited):
          self.amount_deposited=amount_deposited
          self.amount_withdraw=amount_withdraw
          self.balance=balance
          self.account_name=account_name
      def deposit(self):
        self.balance += self.amount_deposited
        return f"Hello {self.account_name} you have withdrawn { self.amount_deposited}your new balance is{   self.balance} " 

      def withdraw(self):
        self.amount_deposited -= self.amount_withdraw
        return f"Hello {self.account_name} you have withdrawn { self.amount_withdraw}your new balance is{   self.balance} " 

         
