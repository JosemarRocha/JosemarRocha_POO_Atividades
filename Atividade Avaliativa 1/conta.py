"""
Autor: Josemar Rocha da Silva
Atividade Avaliativa 1 de POO
Professor: Filipe Dwan
"""

import datetime

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Data:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()

    def imprime_data(self):
        print("data abertura: {}".format(self.data_abertura))

class Historico:
    def __init__(self):
        self.transacoes = []

    def imprime(self):
        print("transacoes: ")
        for t in self.transacoes:
            print("-", t)

class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.data = Data()
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("depósito de {}".format(valor))

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))
            return True

    def extrato(self):
        print("numero: {} \nsaldo: {} \nnome: {} \nsobrenome: {} \ncpf: {}".format(self.numero, self.saldo, self.titular.nome,
                                                                                   self.titular.sobrenome, self.titular.cpf))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    def trasfere_para(self, conta2, valor):
        retirou = self.saca(valor)
        if(retirou == False):
            return False
        else:
            conta2.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para conta {} ".format(valor, conta2.numero))
            return True

