class Account:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def updateBalance(self,balance):
        self.__balance = balance
      
  
    def PrintAccount(self):
        print(self.name)
        print(self.__balance)

    def Spend(self,amount):
        if self.__balance < amount:
            print("STOP SPENDING .. you dont have money")
        else:
            print("You have enough balance")
            self.__balance = self.__balance - amount
            print("New balance is",self.__balance)

