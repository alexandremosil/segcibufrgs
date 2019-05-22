# Ethereum

## Prova de conceito com Ethereum

### Instalação dos requisitos

- [web3.py](https://github.com/ethereum/web3.py) : Interface Python para Ethereum

    - pip install web3

- [Ethereum](https://geth.ethereum.org/) : Implementação oficial do protocolo Ethereum

    - Download e execução do arquivo de instalação (No Windows: geth-windows-amd64-1.8.27-4bcc0a37)

### Observações

O script grava no nó Ethereum local uma lista de 20 votos, retornando o 
json deste processamento voto por voto.

O arquivo poc_ethereum.py contém o script.

O arquivo votacao.sol contém o smart contract para a votação.

O arquivo poc_ethereumn.json contém um exemplo da saída.