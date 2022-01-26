from clases import User
from clases import BankAccount

pablo = User("Pablo","Sepulveda", "p.sepulvedamorande@gmail.com")

cuenta1 = BankAccount(tipo="vista")
cuenta2 = BankAccount(tipo="Corriente")

pablo.agregar_cuenta(cuenta1)
pablo.agregar_cuenta(cuenta2)

pablo.deposito(0,1000)
pablo.deposito(1,800)
pablo.retiro(1,50)

print(len(pablo.accounts))
for cuenta in pablo.accounts:
    print(f"balance:", cuenta.account_balance)