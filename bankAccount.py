class BankAccount:
    def __init__(self,account_owner,account_number,bank,tipo,interes):
        self.account_owner = account_owner
        self.account_number = account_number
        self.bank = bank
        self.type = tipo
        self.account_balance=0
        self.interes = interes

    def deposit(self,amount):
        self.account_balance += amount
        return self

    def withdraw(self,amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"Banco {self.bank} le informa que el Balance de la cuenta {self.type} numero {self.account_number} de {self.account_owner} es de {self.account_balance} Dolares")
        print(f"Los interes anuales a fin del periodo de esta cuanta rondaran los {self.account_balance*self.interes} Dolares")
        return self

    def yield_interest(self):
        self.account_balance += self.account_balance*self.interes
        return self


ps123456 = BankAccount ("Pablo Sepulveda", 123456, "Santander", "corriente",0.005)
mr789101 = BankAccount ("Madalena Rolando", 789101, "Santander Prime", "corriente Premium",0.009)

ps123456.deposit(1000).deposit(1300).withdraw(200).deposit(825).yield_interest()
mr789101.deposit(5000).deposit(11300).withdraw(200).withdraw(800).withdraw(3000).withdraw(500).yield_interest()

ps123456.display_account_info()
mr789101.display_account_info()


