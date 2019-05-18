from hashlib import sha256
from datetime import datetime
from pprint import pprint, PrettyPrinter

# O bloco
class Block:

    # Inicializa um novo bloco
    def __init__(self, transactions, previous_hash):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculateHash()
        self.pow = ''

    # Calcula o hash do bloco
    def calculateHash(self):
        block_hash = (str(self.timestamp) +
                      str(self.transactions) + 
                      str(self.previous_hash) +
                      str(self.nonce))
        return sha256(block_hash.encode()).hexdigest()

    # Obtém o hash do bloco
    def getHash(self):
        return self.hash

    # Obtém o número de transações no bloco
    def getBlockSize(self):
        return len(transactions)

    # Imprime o bloco
    def printBlock(self):
        pp = PrettyPrinter()
        print("===========================================================================================")
        print("Hash...........: " + str(self.getHash()))
        print("Previous hash..: " + str(self.previous_hash))
        print("Proof of Work..: " + str(self.pow))
        print("Timestamp....... " + str(self.timestamp))
        print("Transactions ------------------------------------------------------------------------------")
        pp.pprint(self.transactions)
        print("===========================================================================================")
