# Custom Exception

class LowBalanceExceptionCustom(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


balance = 100
withdraw = int(input("Enter the amount you want to withdraw"))
if withdraw>balance:
    raise LowBalanceExceptionCustom("You do not have enough funds to withdraw")
else:
    print("Remain Balance: ",(balance-withdraw))