#!/usr/bin/python
# -*- codificação: utf-8 -*-

de aleatório importar aleatório,embaralhar


def quadro_de_impressão(quadro):
    """
    Imprime o tabuleiro do sudoku.

    Argumentos:
        tabuleiro (lista[lista[int]]): Um tabuleiro de sudoku 9x9 representado como uma lista de listas de inteiros.

    Retornos:
        Nenhum.
    """

    cadeia de caracteres de tabuleiro = ""
    para eu em faixa(9):
        para eu em faixa(9):
            cadeia de caracteres de tabuleiro += str(quadro[eu][eu])+ " "
            se(eu + 1)% 3 == 0 e eu != 0 e eu + 1 != 9:
                cadeia de caracteres de tabuleiro += "| "

            se eu == 8:
                cadeia de caracteres de tabuleiro += "\n"

            se eu == 8 e(eu + 1)% 3 == 0 e eu + 1 != 9:
                cadeia de caracteres de tabuleiro += "- - - - - - - - - - -\n"
    imprimir(cadeia de caracteres de tabuleiro)


def encontrar_vazio(quadro):
    """
    Encontra uma célula vazia no tabuleiro de sudoku.

    Argumentos:
        tabuleiro (lista[lista[int]]): Um tabuleiro de sudoku 9x9 representado como uma lista de listas de inteiros.

    Retornos:
        tuple[int, int]|None: A posição da primeira célula vazia encontrada como uma tupla de índices de linha e coluna, ou None se nenhuma célula vazia for encontrada.
    """

    para eu em faixa(9):
        para eu em faixa(9):
            se quadro[eu][eu]== 0:
                retornar(eu,eu)
    retornar Nenhum


def válido(quadro,pos,num):
    """
    Verifica se um número é válido em uma célula do tabuleiro de sudoku.

    Argumentos:
        tabuleiro (lista[lista[int]]): Um tabuleiro de sudoku 9x9 representado como uma lista de listas de inteiros.
        pos (tupla[int, int]): A posição da célula a ser verificada como uma tupla de índices de linha e coluna.
        num (int): O número a ser verificado.

    Retornos:
        bool: Verdadeiro se o número for válido na célula, Falso caso contrário.
    """

    para eu em faixa(9):
        se quadro[eu][pos[1]]== num:
            retornar Falso

    para eu em faixa(9):
        se quadro[pos[0]][eu]== num:
            retornar Falso

    início_i = pos[0]- pos[0]% 3
    início_j = pos[1]- pos[1]% 3
    para eu em faixa(3):
        para eu em faixa(3):
            se quadro[início_i + eu][início_j + eu]== num:
                retornar Falso
    retornar Verdadeiro


def resolver(quadro):
    """
    Resolve o tabuleiro de sudoku usando o algoritmo de retrocesso.

    Argumentos:
        tabuleiro (lista[lista[int]]): Um tabuleiro de sudoku 9x9 representado como uma lista de listas de inteiros.

    Retornos:
        bool: Verdadeiro se o tabuleiro de sudoku for solucionável, Falso caso contrário.
    """

    vazio = encontrar_vazio(quadro)
    se não vazio:
        retornar Verdadeiro

    para números em faixa(1,10):
        se válido(quadro,vazio,números):
            quadro[vazio[0]][vazio[1]]= números

            se resolver(quadro):  # passo recursivo
                retornar Verdadeiro
            quadro[vazio[0]][vazio[1]]= 0  # esse número está errado então o colocamos de volta em 0
    retornar Falso


def gerar_placa():
    """
    Gera um tabuleiro de sudoku aleatório com menos números iniciais.

    Retornos:
        list[list[int]]: Um tabuleiro de sudoku 9x9 representado como uma lista de listas de inteiros.
    """

    quadro =[[0 para eu em faixa(9)]para eu em faixa(9)]

    # Preencha as caixas diagonais
    para eu em faixa(0,9,3):
        números = lista(faixa(1,10))
        embaralhar(números)
        para linha em faixa(3):
            para coluna em faixa(3):
                quadro[eu + linha][eu + coluna]= números.estouro()

    # Preencha as células restantes com retrocesso
    def células_de_preenchimento(quadro,linha,coluna):
        """
        Preenche as células restantes do tabuleiro de sudoku com retrocesso.

        Argumentos:
            tabuleiro (lista[lista[int]]): Um tabuleiro de sudoku 9x9 representado como uma lista de listas de inteiros.
            linha (int): O índice da linha atual a ser preenchida.
            col (int): O índice da coluna atual a ser preenchida.

        Retornos:
            bool: Verdadeiro se as células restantes forem preenchidas com sucesso, Falso caso contrário.
        """

        se linha == 9:
            retornar Verdadeiro
        se coluna == 9:
            retornar células_de_preenchimento(quadro,linha + 1,0)

        se quadro[linha][coluna]!= 0:
            retornar células_de_preenchimento(quadro,linha,coluna + 1)

        para num em faixa(1,10):
            se válido(quadro, (linha,coluna),num):
                quadro[linha][coluna]= num

                se células_de_preenchimento(quadro,linha,coluna + 1):
                    retornar Verdadeiro

        quadro[linha][coluna]= 0
        retornar Falso

    células_de_preenchimento(quadro,0,0)

    # Remova um número maior de células para criar um quebra-cabeça com menos números iniciais
    para _ em faixa(aleatório(55,65)):
        linha,coluna = aleatório(0,8),aleatório(0,8)
        quadro[linha][coluna]= 0

    retornar quadro


se __nome__ == "__principal__":
    quadro = gerar_placa()
    quadro_de_impressão(quadro)
    resolver(quadro)
    quadro_de_impressão(quadro)
