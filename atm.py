class atm(object):
    def _init_(self,atmCardNumber,AtmPinNumber):
        self.atmCardNumber=atmCardNumber
        self.AtmPinNumber=AtmPinNumber


    def CashWithdraw(self,cash):
        cash=input('WRITE THE AMOUNT : ')
        print(cash, "Withdraw successfully")

ff=atm(111111111,1234)
print(ff.atmCardNumber)
print(ff.AtmPinNumber)
ff.CashWithdraw(500)