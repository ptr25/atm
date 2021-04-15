class Atm(object):
    def __init__(self,cardNumber,pinNumber):
          self.cardNumber= cardNumber
          self.pinNumber= pinNumber
    def cashWithdrawal(self):
        print("Cash Withdrawed")
    def balanceEnquiry(self):
        print("Your Balance Statement has been sent to your registered mobile number")
    def balanceWithdrawal(self):
        print("Balance Withdrawed")
    def deposit(self):
        print("Cash Deposited")

customer = Atm(12080937,1010)
