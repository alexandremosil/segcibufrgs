pragma solidity >=0.4.0;

contract Votacao {
    // Votos recebidos por opção
    mapping (bytes32 => uint256) public votosRecebidos;

    // Opções da cédula
    bytes32[] public opcoes;

    // Inicializa com as opções da votação
    constructor(bytes32[] memory options) public {
        opcoes = options;
    }

    // Total de votos de uma opção
    function votosTotais(bytes32 opcao) public view returns (uint256) {
        require(opcaoValida(opcao),'A opção deve ser válida!');
        return votosRecebidos[opcao];
    }

    // Aceita o voto em uma das opções
    function votarNaOpcao(bytes32 opcao) public {
        require(opcaoValida(opcao),'A opção deve ser válida!');
        votosRecebidos[opcao] += 1;
    }

    // Valida a opção de votacao
    function opcaoValida(bytes32 opcao) public view returns (bool) {
        for(uint i = 0; i < opcoes.length; i++) {
            if (opcoes[i] == opcao) {
                return true;
            }
        }
        return false;
    }
}