#!/usr/bin/python
# -*- codificação: utf-8 -*-
de ferramentas de sudoku importar válido,resolver,encontrar_vazio,gerar_placa
de cópia importar cópia profunda
de sistema importar saída
importar jogo de py
importar tempo
importar aleatório

jogo de py.iniciar()


aula Quadro:
    def __iniciar__(auto,janela):
        """
        Inicializa um objeto Board.

        Argumentos:
            window: O objeto de janela do Pygame.
        """
        # Gere um novo tabuleiro de Sudoku e crie uma versão resolvida dele.
        auto.quadro = gerar_placa()
        auto.Quadro resolvido = cópia profunda(auto.quadro)
        resolver(auto.Quadro resolvido)
        # Crie uma lista 2D de objetos Tile para representar o tabuleiro de Sudoku.
        auto.azulejos =[
            [Telha(auto.quadro[eu][eu],janela,eu * 60,eu * 60)para eu em faixa(9)]
            para eu em faixa(9)
        ]
        auto.janela = janela

    def prancheta(auto):
        """
        Desenha o tabuleiro de Sudoku na janela do Pygame.
        """
        para eu em faixa(9):
            para eu em faixa(9):
                # Desenhe linhas verticais a cada três colunas.
                se eu % 3 == 0 e eu != 0:
                    jogo de py.empate.linha(
                        auto.janela,
                        (0,0,0),
                        (eu // 3 * 180,0),
                        (eu // 3 * 180,540),
                        4,
                    )
                # Desenhe linhas horizontais a cada três linhas.
                se eu % 3 == 0 e eu != 0:
                    jogo de py.empate.linha(
                        auto.janela,
                        (0,0,0),
                        (0,eu // 3 * 180),
                        (540,eu // 3 * 180),
                        4,
                    )
                # Desenhe o objeto Tile no tabuleiro.
                auto.azulejos[eu][eu].empate((0,0,0),1)

                # Exibe o valor do Tile se não for 0 (vazio).
                se auto.azulejos[eu][eu].valor != 0:
                    auto.azulejos[eu][eu].mostrar(
                        auto.azulejos[eu][eu].valor, (21 + eu * 60,16 + eu * 60), (0,0,0)
                    )
        # Desenhe uma linha horizontal na parte inferior do quadro.
        jogo de py.empate.linha(
            auto.janela,
            (0,0,0),
            (0, (eu + 1)// 3 * 180),
            (540, (eu + 1)// 3 * 180),
            4,
        )

    def desmarcar(auto,telha):
        """
        Desmarca todos os blocos, exceto o bloco fornecido.

        Argumentos:
            tile (Tile): O tile que deve permanecer selecionado.

        Retornos:
            Nenhum
        """
        para eu em faixa(9):
            para eu em faixa(9):
                se auto.azulejos[eu][eu]!= telha:
                    auto.azulejos[eu][eu].selecionado = Falso

    def redesenhar(auto,chaves,errado,tempo):
        """
        Redesenha o tabuleiro do Sudoku na janela do jogo, destacando as peças selecionadas, corretas e incorretas, exibindo o
        contagem e tempo errados atuais e renderização das chaves atuais (valores potenciais) para cada bloco.

        Argumentos:
            chaves (dict): Um dicionário contendo tuplas de coordenadas (x, y) como chaves e valores potenciais como valores.
            errado (int): A contagem errada atual.
            tempo (int): O tempo decorrido atual.

        Retornos:
            Nenhum
        """
        auto.janela.preencher((255,255,255))  # preencha a janela com branco
        auto.prancheta()  # desenhe o tabuleiro do Sudoku
        para eu em faixa(9):
            para eu em faixa(9):
                se auto.azulejos[eu][eu].selecionado:
                    # destacar os blocos selecionados em verde
                    auto.azulejos[eu][eu].empate((50,205,50),4)
                elif auto.azulejos[eu][eu].correto:
                    # destacar os blocos corretos em verde escuro
                    auto.azulejos[eu][eu].empate((34,139,34),4)
                elif auto.azulejos[eu][eu].incorreto:
                    # destacar os blocos incorretos em vermelho
                    auto.azulejos[eu][eu].empate((255,0,0),4)

        se Lenta(chaves)!= 0:
            para valor em chaves:
                # exibir os valores potenciais para cada bloco
                auto.azulejos[valor[0]][valor[1]].mostrar(
                    chaves[valor],
                    (21 + valor[0]* 60,16 + valor[1]* 60),
                    (128,128,128),
                )

        se errado > 0:
            # exibe a contagem errada atual como um ícone "X" e um número
            fonte = jogo de py.fonte.Fonte do sistema("Bauhaus 93",30)
            texto = fonte.render("X",Verdadeiro, (255,0,0))
            auto.janela.blit(texto, (10,554))

            fonte = jogo de py.fonte.Fonte do sistema("Escrita ferroviária",40)
            texto = fonte.render(str(errado),Verdadeiro, (0,0,0))
            auto.janela.blit(texto, (32,542))

        # exibe o tempo decorrido atual como um número
        fonte = jogo de py.fonte.Fonte do sistema("Escrita ferroviária",40)
        texto = fonte.render(str(tempo),Verdadeiro, (0,0,0))
        auto.janela.blit(texto, (388,542))
        jogo de py.mostrar.virar()  # atualizar a janela do jogo

    def Solução visual(auto,errado,tempo):
        """
        Resolve recursivamente o tabuleiro de Sudoku visualmente, destacando as peças corretas e incorretas à medida que as preenche.

        Argumentos:
            errado (int): A contagem errada atual.
            tempo (int): O tempo decorrido atual.

        Retornos:
            bool: Verdadeiro se o problema for resolvido com sucesso, Falso caso contrário.
        """
        para evento em jogo de py.evento.pegar():
            se evento.tipo == jogo de py.DESISTIR:
                saída()  # sair do jogo se o usuário clicar no botão fechar

        vazio = encontrar_vazio(auto.quadro)
        se não vazio:
            retornar Verdadeiro  # o tabuleiro é resolvido se não houver mais peças vazias

        para números em faixa(9):
            se válido(auto.quadro, (vazio[0],vazio[1]),números + 1):
                # preencha o bloco vazio atual com um número válido
                auto.quadro[vazio[0]][vazio[1]]= números + 1
                auto.azulejos[vazio[0]][vazio[1]].valor = números + 1
                auto.azulejos[vazio[0]][vazio[1]].correto = Verdadeiro
                jogo de py.tempo.atraso(63)  # delay para desacelerar a animação de resolução
                auto.redesenhar(
                    {},errado,tempo
                )  # redesenhar a janela do jogo com o tabuleiro atualizado

                se auto.Solução visual(errado,tempo):
                    retornar Verdadeiro  # resolver recursivamente o resto do tabuleiro se o movimento atual for válido

                # se o movimento atual não for válido, reinicie o bloco e destaque-o como incorreto
                auto.quadro[vazio[0]][vazio[1]]= 0
                auto.azulejos[vazio[0]][vazio[1]].valor = 0
                auto.azulejos[vazio[0]][vazio[1]].incorreto = Verdadeiro
                auto.azulejos[vazio[0]][vazio[1]].correto = Falso
                jogo de py.tempo.atraso(63)  # delay para desacelerar a animação de resolução
                auto.redesenhar(
                    {},errado,tempo
                )  # redesenhar a janela do jogo com o tabuleiro atualizado

    def dica(auto,chaves):
        """
        Fornece uma dica preenchendo uma peça vazia aleatória com o número correto.

        Argumentos:
            chaves (dict): Um dicionário contendo tuplas de coordenadas (x, y) como chaves e valores potenciais como valores.

        Retornos:
            bool: Verdadeiro se uma dica for fornecida com sucesso, Falso se o tabuleiro já estiver resolvido.
        """
        enquanto Verdadeiro:
            eu = aleatório.aleatório(0,8)
            eu = aleatório.aleatório(0,8)
            se auto.quadro[eu][eu]== 0:
                se(eu,eu)em chaves:
                    do chaves[(eu,eu)]
                # preencha o bloco vazio selecionado com o número correto
                auto.quadro[eu][eu]= auto.Quadro resolvido[eu][eu]
                auto.azulejos[eu][eu].valor = auto.Quadro resolvido[eu][eu]
                retornar Verdadeiro
            elif auto.quadro == auto.Quadro resolvido:
                retornar Falso  # o tabuleiro já está resolvido, então nenhuma dica pode ser fornecida.


aula Telha:
    def __iniciar__(
        auto,
        valor,
        janela,
        x1,
        y1,
    ):
        """
        Inicializa um objeto Tile.

        Argumentos:
            valor (int): O valor a ser exibido no Tile.
            janela (pygame.Surface): A superfície para desenhar o Tile.
            x1 (int): A coordenada x do canto superior esquerdo do Tile.
            y1 (int): A coordenada y do canto superior esquerdo do Tile.

        Atributos:
            valor (int): O valor a ser exibido no Tile.
            janela (pygame.Surface): A superfície para desenhar o Tile.
            rect (pygame.Rect): A área retangular do Tile.
            selecionado (bool): Se o Tile está selecionado no momento.
            correto (bool): Se o valor no Tile está correto.
            incorreto (bool): Se o valor no Tile está incorreto.
        """

        auto.valor = valor
        auto.janela = janela
        auto.reto = jogo de py.Retângulo(x1,y1,60,60)
        auto.selecionado = Falso
        auto.correto = Falso
        auto.incorreto = Falso

    def empate(auto,cor,grossura):
        """
        Desenha o Tile na janela com uma borda colorida.

        Argumentos:
            cor (tupla[int, int, int]): O valor da cor RGB da borda.
            espessura (int): A espessura da borda.

        Retornos:
            Nenhum.
        """

        jogo de py.empate.reto(auto.janela,cor,auto.reto,grossura)

    def mostrar(
        auto,
        valor,
        posição,
        cor,
    ):
        """
        Exibe o valor do Tile no centro do Tile.

        Argumentos:
            valor (int): O valor a ser exibido.
            posição (tupla[int, int]): As coordenadas (x, y) do centro do Tile.
            cor (tupla[int, int, int]): O valor da cor RGB do texto.

        Retornos:
            Nenhum.
        """

        fonte = jogo de py.fonte.Fonte do sistema("lato",45)
        texto = fonte.render(str(valor),Verdadeiro,cor)
        auto.janela.blit(texto,posição)

    def clicado(auto,mousePos):
        """
        Verifica se o Tile foi clicado pelo mouse.

        Argumentos:
            mousePos (tuple[int, int]): As coordenadas (x, y) do mouse.

        Retornos:
            bool: Verdadeiro se o bloco for clicado, Falso caso contrário.
        """

        se auto.reto.ponto de colisão(mousePos):
            auto.selecionado = Verdadeiro
        retornar auto.selecionado


def principal():
    # Configurar a janela do pygame
    tela = jogo de py.mostrar.modo_de_configuração((540,590))
    tela.preencher((255,255,255))
    jogo de py.mostrar.definir_legenda("Resolução de Sudoku")
    ícone = jogo de py.imagem.carregar("ativos/thumbnail.png")
    jogo de py.mostrar.conjunto_ícone(ícone)

    # Exibir texto "Gerando grade aleatória" ao gerar uma grade aleatória
    fonte = jogo de py.fonte.Fonte do sistema("Escrita ferroviária",40)
    texto = fonte.render("Gerando",Verdadeiro, (0,0,0))
    tela.blit(texto, (175,245))

    fonte = jogo de py.fonte.Fonte do sistema("Escrita ferroviária",40)
    texto = fonte.render("Grade aleatória",Verdadeiro, (0,0,0))
    tela.blit(texto, (156,290))
    jogo de py.mostrar.virar()

    # Inicializar variáveis
    errado = 0
    quadro = Quadro(tela)
    selecionado =(-1,-1)
    chaveDict ={}
    resolvido = Falso
    hora de início = tempo.tempo()

    # Repita até que o sudoku seja resolvido
    enquanto não resolvido:
        # Obter o tempo decorrido e formatá-lo para exibir na janela
        decorrido = tempo.tempo()- hora de início
        tempopassado = tempo.tempo de luta("%H:%M:%S",tempo.hora gm(decorrido))

        # Verifique se o sudoku foi resolvido
        se quadro.quadro == quadro.Quadro resolvido:
            resolvido = Verdadeiro

        # Manipular eventos
        para evento em jogo de py.evento.pegar():
            decorrido = tempo.tempo()- hora de início
            tempopassado = tempo.tempo de luta("%H:%M:%S",tempo.hora gm(decorrido))
            se evento.tipo == jogo de py.DESISTIR:
                saída()
            elif evento.tipo == jogo de py.BOTÃO DO MOUSE PARA CIMA:
                # Verifique se um Tile foi clicado
                mousePos = jogo de py.rato.obter_pos()
                para eu em faixa(9):
                    para eu em faixa(9):
                        se quadro.azulejos[eu][eu].clicado(mousePos):
                            selecionado =(eu,eu)
                            quadro.desmarcar(quadro.azulejos[eu][eu])
            elif evento.tipo == jogo de py.TECLA PARA BAIXO:
                # Lidar com pressionamentos de tecla
                se quadro.quadro[selecionado[1]][selecionado[0]]== 0 e selecionado !=(-1,-1):
                    se evento.chave == jogo de py.K_1:
                        chaveDict[selecionado]= 1

                    se evento.chave == jogo de py.K_2:
                        chaveDict[selecionado]= 2

                    se evento.chave == jogo de py.K_3:
                        chaveDict[selecionado]= 3

                    se evento.chave == jogo de py.K_4:
                        chaveDict[selecionado]= 4

                    se evento.chave == jogo de py.K_5:
                        chaveDict[selecionado]= 5

                    se evento.chave == jogo de py.K_6:
                        chaveDict[selecionado]= 6

                    se evento.chave == jogo de py.K_7:
                        chaveDict[selecionado]= 7

                    se evento.chave == jogo de py.K_8:
                        chaveDict[selecionado]= 8

                    se evento.chave == jogo de py.K_9:
                        chaveDict[selecionado]= 9
                    elif(
                        evento.chave == jogo de py.K_RETROCESSO ou evento.chave == jogo de py.K_EXCLUIR
                    ):
                        se selecionado em chaveDict:
                            quadro.azulejos[selecionado[1]][selecionado[0]].valor = 0
                            do chaveDict[selecionado]
                    elif evento.chave == jogo de py.K_RETORNO:
                        se selecionado em chaveDict:
                            se(
                                chaveDict[selecionado]
                                != quadro.Quadro resolvido[selecionado[1]][selecionado[0]]
                            ):
                                errado += 1
                                quadro.azulejos[selecionado[1]][selecionado[0]].valor = 0
                                do chaveDict[selecionado]
                                # quebrar

                            quadro.azulejos[selecionado[1]][selecionado[0]].valor = chaveDict[
                                selecionado
                            ]
                            quadro.quadro[selecionado[1]][selecionado[0]]= chaveDict[selecionado]
                            do chaveDict[selecionado]

                # Chave de dica de manuseio
                se evento.chave == jogo de py.K_h:
                    quadro.dica(chaveDict)

                # Lidar com a tecla de espaço
                se evento.chave == jogo de py.K_ESPAÇO:
                    # Desmarque todos os blocos e limpe keyDict
                    para eu em faixa(9):
                        para eu em faixa(9):
                            quadro.azulejos[eu][eu].selecionado = Falso
                    chaveDict ={}

                    # Resolva o sudoku visualmente e redefina a correção de todas as peças
                    decorrido = tempo.tempo()- hora de início
                    tempopassado = tempo.tempo de luta("%H:%M:%S",tempo.hora gm(decorrido))
                    quadro.Solução visual(errado,tempopassado)
                    para eu em faixa(9):
                        para eu em faixa(9):
                            quadro.azulejos[eu][eu].correto = Falso
                            quadro.azulejos[eu][eu].incorreto = Falso

                    # Defina resolvido como Verdadeiro após resolver o sudoku:
                    resolvido = Verdadeiro

        quadro.redesenhar(chaveDict,errado,tempopassado)
    enquanto Verdadeiro:
        para evento em jogo de py.evento.pegar():
            se evento.tipo == jogo de py.DESISTIR:
                retornar


principal()
jogo de py.desistir()
