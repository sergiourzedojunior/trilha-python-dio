from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def registrar(self, conta):
        conta.saldo += self.valor
        print(f"Depósito de R$ {self.valor:.2f} realizado com sucesso!")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def registrar(self, conta):
        if self.valor > 0 and self.valor <= conta.saldo:
            conta.saldo -= self.valor
            print(f"Saque de R$ {self.valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta(ABC):
    def __init__(self, numero, agencia, cliente, saldo=0):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = saldo
        self._historico = Historico()

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)
        self._historico.adicionar_transacao(deposito)

    def exibir_extrato(self):
        print(f"Extrato da conta {self.numero}")
        for transacao in self._historico.transacoes:
            print(f"- {transacao.data}: {type(transacao).__name__} de R$ {transacao.valor:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, saldo=0, limite=500):
        super().__init__(numero, agencia, cliente, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > 0 and valor <= (self.saldo + self.limite):
            saque = Saque(valor)
            saque.registrar(self)
            self._historico.adicionar_transacao(saque)
        else:
            print("Saldo/limite insuficiente ou valor inválido para saque.")
