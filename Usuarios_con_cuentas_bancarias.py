class BankAccount:
    def __init__(self,number,balance=0):
        self.number = number
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Banco {self.bank} le informa que el Balance de la cuenta {self.type} numero {self.account_number} de {self.account_owner} es de {self.account_balance} Dolares")
        print(f"Los interes anuales a fin del periodo de esta cuanta rondaran los {self.account_balance*self.interes} Dolares")
        return self

    def yield_interest(self):
        self.account += self.balance*self.interes
        return self

ps123456 = BankAccount (123456) #Consultar mañana por que lu numero de cuenta no viene

class User:
    def __init__(self, username,lastName,email_address):    
        self.name = username
        self.lastName = lastName			                                   
        self.email = email_address		                                   
        self.account = BankAccount(number=0 ,balance=0)

pablo = User("Pablo","Sepulveda", "p.sepulvedamorande@gmail.com")

print(pablo.name)
print(pablo.lastName)
print(pablo.account.balance)
print(pablo.account.number)
pablo.account.deposit(100)
print(pablo.account.balance)



