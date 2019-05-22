from web3.auto import w3

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
    pass

# entry point
if __name__ == "__main__":
    main()