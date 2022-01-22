class User:
    def __init__(self, username,lastName, email_address):    # ahora nuestro método tiene 2 parametros!
        self.name = username
        self.lastName = lastName			                                   #y usamos los valores pasados para establecer el atributo de nombre
        self.email = email_address		                                   # y el atributo email
        self.account_balance = 0                # el saldo de la cuenta se establece en $ 0, así que no es necesario un tercer parámetro

    def deposito(self,amount=0):
        self.account_balance += amount
        return self

    def retiro(self, amount=0):
        self.account_balance -= amount
        return self

    def balance(self):
        print(f"El Balance de {self.name} {self.lastName} es {self.account_balance} Dolares")
        return self


pablo = User("Pablo","Sepulveda", "p.sepulvedamorande@gmail.com")
magdalena = User("Magdalena","Rolando", "magdalena@gmail.com")
juan = User ("Juan","Juani", "juan@gmail.com")

print(pablo.account_balance)
print(magdalena.account_balance)
print(juan.account_balance)

pablo.deposito(100).deposito(100).retiro(80).deposito(100).deposito(100).retiro(25).balance()
magdalena.deposito(1000).retiro(500).balance()
juan.deposito(100).deposito(100).deposito(100).retiro(57).balance()
