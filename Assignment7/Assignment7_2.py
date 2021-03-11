class BankAccount:
    ROI=10.5
    def __init__(self, nameValue, amountValue):
        self.Name=nameValue
        self.Amount=amountValue
    
    def Display(self):
        print("Bank Account Balance of {} is {}".format(self.Name,self.Amount))

    def Deposit(self):
        print("Enter Amount to Deposit")
        amount = int(input())
        self.Amount = self.Amount + amount

    def Withdraw(self):
        print("Enter Amount to Withdraw")
        amount = int(input())
        self.Amount = self.Amount - amount

    def CalculateIntrest(self):
        intrest = (self.Amount * BankAccount.ROI*1)/100
        print("Calculated Return on investment is",intrest)

def main():
    print("Enter Name")
    name=input()
    print("Enter Amount")
    amount=int(input())
    Obj1=BankAccount(name, amount)
    Obj1.Display()
    Obj1.Deposit()
    Obj1.Display()
    Obj1.Withdraw()
    Obj1.Display()
    Obj1.CalculateIntrest()

    print("Enter Name")
    name=input()
    print("Enter Amount")
    amount=int(input())
    Obj2=BankAccount(name, amount)
    Obj2.Display()
    Obj2.Deposit()
    Obj2.Display()
    Obj2.Withdraw()
    Obj2.Display()
    Obj2.CalculateIntrest()

if __name__=="__main__":
    main()

    