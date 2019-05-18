import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

from hashlib import sha256
from time import time, ctime
from pprint import pprint, PrettyPrinter

from core import *

def main():

    # Impressão mais amigável
    pp = PrettyPrinter()

    # Obtém os eleitores aptos
    eleitores = get_eleitores()

    # Acrescenta as chaves públicas e privadas à lista de eleitores (simula carteira)
    eleitores = gera_carteiras(eleitores)

    # Gera 4 listas de transações com 5 votos cada (4 blocos na cadeia)
    transactions_1 = []
    for v in range(0,5):
        transactions_1.append({'id':eleitores[v]['id'],'voto':eleitores[v]['voto']})

    transactions_2 = []
    for v in range(5,10):
        transactions_2.append({'id':eleitores[v]['id'],'voto':eleitores[v]['voto']})

    transactions_3 = []
    for v in range(10,15):
        transactions_3.append({'id':eleitores[v]['id'],'voto':eleitores[v]['voto']})

    transactions_4 = []
    for v in range(15,20):
        transactions_4.append({'id':eleitores[v]['id'],'voto':eleitores[v]['voto']})

    # Cria a cadeia
    blockchain = Blockchain('Blockchain teste votação')
    
    # Acrescenta as transações à cadeia
    blockchain.addBlock(transactions_1)
    blockchain.addBlock(transactions_2)
    blockchain.addBlock(transactions_3)
    blockchain.addBlock(transactions_4)

    # Imprime a cadeia com as transações
    blockchain.printBlockchain()

    # Valida a cadeia pelos hashs dos blocos
    blockchain.validateChain()

    # Altera uma transação diretamente na cadeia, imprime e tenta validar
    blockchain.chain[2].transactions[1] = {'ID':'666','VOTO':'666'}
    blockchain.printBlockchain()
    blockchain.validateChain()

# entry point
if __name__ == "__main__":
    main()
