from hashlib import sha256
from time import time, ctime
from pprint import pprint, PrettyPrinter
from .Block import Block

# A cadeia
class Blockchain:

    # Inicializa a cadeia
    def __init__(self, metadata):
        self.metadata = [{'metadata' : metadata}]
        self.unconfirmed_transactions = []
        self.chain = []
        self.index = 0
        self.startGenesisBlock()

    # Cria o bloco genesis
    def startGenesisBlock(self):
        transactions = []
        self.metadata.append({
            'block_type': 'genesis',
            'genesis 1:1': 'No princípio Deus criou os céus e a terra.',
        })
        genesis_block = Block(transactions, 0)
        self.chain.append(genesis_block)

    # Obtém o tamanho da cadeia
    def getBlockchainSize(self):
        return len(self.chain)

    # Adiciona um novo bloco à cadeia
    def addBlock(self, transactions):
        previous_hash = (self.chain[len(self.chain)-1]).hash
        new_block = Block(transactions, previous_hash)
        new_block.getHash()
        pow = self.proofOfWork(new_block)
        new_block.pow = pow
        self.chain.append(new_block)
        return pow, new_block

    # Imprime a cadeia
    def printBlockchain(self):
        pp = PrettyPrinter()
        print("===========================================================================================")
        pp.pprint(self.metadata)
        print("===========================================================================================")
        for b in self.chain:
            b.printBlock()

    # Prova de trabalho       
    def proofOfWork(self, block, difficulty = 2): 
        pow = block.getHash()
        while pow[:difficulty] != '0' * difficulty:
            block.nonce += 1
            pow = block.calculateHash()
        block.nonce = 0
        return pow

    # Valida a cadeia
    def validateChain(self):
        for i in range(1, self.getBlockchainSize()):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            if(current.hash != current.calculateHash()):
                print("Erro no hash do bloco atual : " + str(current.hash))
                print("O hash atual: " + str(current.calculateHash()))
                return False
            
            if(current.previous_hash != previous.calculateHash()):
                print("Erro no hash do bloco anterior : " + str(current.previous_hash))
                return False

        print("A cadeia foi validada com sucesso!")
        return True
