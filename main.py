from dataclasses import dataclass

maximo: int = 3
@dataclass
class Point:
    dados = []
    inicio: int = 0
    topo: int = 0

p = Point

def inserir_dados():
    if maximo == p.topo:
        print("A pilha está cheia")
        input()

    else:
        p.dados.append(int(input("Digite o valor a ser empilhado: ")))
        p.topo += 1

def retirar_dados():
    if p.topo == p.inicio:
        print("A pilha está vazia")
        input()

    else:
        saida = p.dados
        p.dados[p.topo] = 0
        p.topo -= 1
        return saida

sair: int = 0
while sair != 1:
    opcao = int(input("**********MENU**********\nDigite o numero correspondente a opção desejada\n1 - Adicionar dados\n2 - Retirar e retornar o dado\n"))
    if opcao == 1:
        inserir_dados()
    if opcao == 2:
        retirar_dados()

    sair = int(input("Deseja sair? (1 - Sim/ 2 - Não)\n"))
exit()

