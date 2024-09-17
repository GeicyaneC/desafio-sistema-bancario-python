
# DESAFIO 1 | SISTEMA BANCÁRIO - PYTHON

Este é um projeto simples de um sistema bancário em Python, que permite operações básicas como depósito, saque, consulta de saldo e visualização de extratos. O projeto foi desenvolvido com o objetivo de praticar conceitos de programação como variáveis globais, funções e manipulação de listas.

## 🔧 FUNCIONALIDADES

- Depósitos
- Saques
- Extratos
- Saldos

## 💻REQUISITOS

Este projeto é um script Python simples, sem dependências externas, exceto o Python 3.x.

## Estrutura de Código


```
- saldo(): Exibe o saldo atual da conta.
- deposito(valor): Adiciona o valor depositado ao saldo bancário e armazena a transação na lista de depósitos.
- saque(valor): Subtrai o valor do saldo, verifica o limite de saques e o limite de valor por saque, e armazena a transação na lista de saques.

```
### Regras de Saque
Máximo de 3 saques por dia.

Valor máximo por saque: R$ 500,00.

O sistema avisa se o saldo for insuficiente para o saque.

### Regras de Depósito
O depósito só é permitido se o valor for maior que zero.

## Contribuições
Sinta-se à vontade para sugerir melhorias ou correções. Você pode abrir uma issue ou fazer um pull request neste repositório.
