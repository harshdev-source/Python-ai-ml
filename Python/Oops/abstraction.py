class BankAccount:
    def __init__(self, name, balance):
        self.name = name #Public 
        self._balance = balance  #Protected -> Can be used outside the class but should not be used as per the convention
        self.__balance = balance  #Private -> Can be used using getters and setters 
    
    def get_balance(self):  #Getter
        return self.__balance
    
    def set_balance(self, newbalance):  #Setter
        self.__balance = newbalance


acc1 = BankAccount("Rahul kumar" , 1_00_000)
acc2 = BankAccount("Aparajita", 5_00_000)

acc2.set_balance(10_00_000)

print(acc1.name, acc1.get_balance())
print(acc2.name, acc2.get_balance())

# we still can access the private variable by using object._classname__attribute

print(acc2.name, acc2._BankAccount__balance)