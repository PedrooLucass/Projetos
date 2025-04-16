from random import randint                                          
from termcolor import colored                                       
from time import sleep              
"""
Para facilitar a compreensão, aqui estarão 3 números importantes,
0 são espaços vazios
1 são espaços "sujos", que devem se tornar zeros
2 é um espaço único, o limpador, que transformará espaços 1 em 0, 
será nosso agente reativo, então daremos o nome de aspirador
"""
def imprimir(matriz):                                        
    for valor in matriz:                                            
        for valor2 in valor:                                         
            print(valor2, end=" ")                                   
        print()

def verificar_num(frase):
    while True:

        try:
            valor = int(input(frase))
            if valor >= 0:
                break
            else: 
                print("Tente novamente")
        except:
            print("Tente novamente")
    return valor

def procurando_sujo(matriz, num, num2):
    alcance = 1
    coordenadas_sujos = []
    combinacoes_X = [-1 , +1] # - e +
    combinacoes_Xalcance = [-1, 0, 1]
    combinacoes_Y = [-1 , +1]
    combinacoes_Yalcance = [-1, 0, 1]

    for x in range(0, num):
        for y in range(0, num2):
            if matriz[x][y] == colored(2, 'white'):
                x_aspirador = x
                y_aspirador = y

    while True:
        for x in range(0, num):
            for y in range(0, num2):

                if matriz[x][y] == colored(1, 'red'):

                    for cx in combinacoes_X:
                        for cxa in combinacoes_Xalcance:
                            for cy in combinacoes_Y:
                                for cya in combinacoes_Yalcance:
                                    if (cx * x) + x_aspirador == cxa and (cy * y) + y_aspirador == cya:
                                        coordenadas_sujos.append([x, y])

        if len(coordenadas_sujos) == 0:
            alcance += 1
            combinacoes_Xalcance.append(alcance)
            combinacoes_Xalcance.append(alcance * -1)
            combinacoes_Yalcance.append(alcance)
            combinacoes_Yalcance.append(alcance * -1)
        else:
            break

    return coordenadas_sujos

def andar(matriz, novo_x, novo_y):

    for x in range(0, num):
        for y in range(0, num2):

            if matriz[x][y] == colored(2, 'white'):
                matriz[x][y] = colored(0, 'green')

    matriz[novo_x][novo_y] = colored(2, "white")

    return matriz

def hora_de_parar(matriz):
    hora_de_parar = True

    for x in range(0, num):
        for y in range(0, num2):

            if matriz[x][y] == colored(1, 'red'):
                hora_de_parar = False

    return hora_de_parar

#### INICIO APLICAÇÃO

while True:                                   
    matriz = []                                                   
    lista1 = []  

    print("Digite 0 para parar")
    num = verificar_num("Digite um numero para a linha da matriz: ")
    num2 = verificar_num("Digite um numero para a coluna da matriz: ")

    # PARAR CÓDIGO
    if num == 0 or num2 == 0:                        
        break

    print("\n=-=-= AREA SUJA =-=-=")
    for l in range(0, num):          #### Criando a matriz de forma aleatória
        for c in range(0, num2):
            valor = randint(0, 1)                                   

            if valor == 0:                                           
                lista1.append(colored(valor, 'green'))              
            else:
                lista1.append(colored(valor, 'red'))                 

        lista2 = lista1.copy()                                       
        matriz.append(lista2)                                     
        lista1.clear()  

    x_aspirador = randint(0, num - 1)
    y_aspirador = randint(0, num2 - 1)                        # Criando aspirador
    matriz[x_aspirador][y_aspirador] = colored(2, 'white')
    # aspirador e matriz criados

    imprimir(matriz)

    print("\n=-=-= LIMPEZA =-=-=")

    while True:
        coordenadas_sujos = procurando_sujo(matriz, num, num2)

        try:
            nova_posicao = randint(0, len(coordenadas_sujos)- 1)
        except:
            nova_posicao = randint(0, len(coordenadas_sujos)+ 1)
        try:
            matriz = andar(matriz, coordenadas_sujos[nova_posicao][0], coordenadas_sujos[nova_posicao][1])
        except:
            print(coordenadas_sujos)
            print(nova_posicao)
            break
        imprimir(matriz)
        if hora_de_parar(matriz):
            break
        sleep(1)
        print('---------------------------------------')
