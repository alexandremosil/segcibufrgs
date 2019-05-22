# Importa bilbiotecas necessárias
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
import json

def get_eleitores():
    """ Retorna lista de dados para teste """
    eleitores = [
        {'id':'001','nome':'Paulo','voto':'1'},
        {'id':'002','nome':'Maria','voto':'1'},
        {'id':'003','nome':'Ana','voto':'1'},
        {'id':'004','nome':'Julia','voto':'3'},
        {'id':'005','nome':'Esther','voto':'1'},
        {'id':'006','nome':'Jonas','voto':'1'},
        {'id':'007','nome':'Patricia','voto':'1'},
        {'id':'008','nome':'Alexandre','voto':'4'},
        {'id':'009','nome':'Mario','voto':'1'},
        {'id':'010','nome':'Carlos','voto':'3'},
        {'id':'011','nome':'Pedro','voto':'1'},
        {'id':'012','nome':'Pietra','voto':'2'},
        {'id':'013','nome':'Paula','voto':'1'},
        {'id':'014','nome':'Adriana','voto':'1'},
        {'id':'015','nome':'Debora','voto':'3'},
        {'id':'016','nome':'Regina','voto':'1'},
        {'id':'017','nome':'Francisco','voto':'1'},
        {'id':'018','nome':'Lianna','voto':'4'},
        {'id':'019','nome':'Miguel','voto':'3'},
        {'id':'020','nome':'Sergio','voto':'2'},        
    ]
    return eleitores

def main():
    # Conecta ao nó de teste do BigchainDB
    bdb = BigchainDB('https://test.bigchaindb.com')

    # Gera o par de chaves para o sistema gravar as informações no banco de dados Blockchain
    evoting = generate_keypair()

    eleitores = get_eleitores()

    votos_computados = []

    for i in range(0,len(eleitores)-1):
    
        voto =  bdb.transactions.prepare(
                operation = 'CREATE',
                signers = evoting.public_key,
                asset = {'data': { 'id': eleitores[i]['id'],
                                'nome': eleitores[i]['nome'],
                                'voto': eleitores[i]['voto']}})

        voto_assinado = bdb.transactions.fulfill(
                        voto,
                        private_keys = evoting.private_key)

        voto_enviado = bdb.transactions.send_commit(voto_assinado)
        
        votos_computados.append(voto_enviado)

    
    # Imprime as informações gravadas no banco de dados Blockchain
    print(json.dumps(votos_computados, sort_keys=True, indent=4))

# entry point
if __name__ == "__main__":
    main()