class ContaBancaria : 
    #Construtor
    def __init__(self,cliente,saldo,agencia):
        self.cliente= cliente
        self.saldo_inicial= saldo
        self.agencia= agencia
        self.emprestimo = False

    def depositar(self,valor):
        self.saldo_inicial = self.saldo_inicial + valor

    def levantar(self,valor):
        if self.saldo_inicial > valor:
            self.saldo_inicial = self.saldo_inicial - valor
        else:
            print("Saldo insuficiente")

c1 = ContaBancaria("Filipe",1000,"Famalicao")
c2 = ContaBancaria("Lucas",1000,"Santo Tirso")
c2.depositar(200)
c2.levantar(1000)
print("Saldo da conta :",c2.saldo_inicial)
c2.levantar(300)