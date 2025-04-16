import json
try:
    with open('arquivo.json', 'r'):
        pass
except:
    with open('arquivo.json', 'w') as arquivo:
        objeto = {
            "estudantes" : [],
            "professores" : [],
            "disciplinas" : [],
            "turmas" : [],
            "matriculas" : []
        }
        json.dump(objeto, arquivo)
def verificar_num(minimo=False, maximo=False):
    while True:
        try:
            num = int(input('Digite aqui: '))
            if minimo == False and maximo == False:
                break
            if minimo is not False and maximo == False:
                if num >= minimo:
                    break
                else:
                    print('Seu número é menor que o minimo aceito. Tente novamente.')
            if minimo == False and maximo is not False:
                if num >= maximo:
                    break
                else:
                    print('Seu número é maior que o maximo aceito. Tente novamente.')
            if minimo is not False and maximo is not False:
                if num >= minimo and num <= maximo:
                    break
                else:
                    print('Seu número está fora das opções, por favor tente novamente.')
        except:
            print('Por favor, tente novamente, apenas com números.')
    return num
def conferir(objeto, chave=str, endereco=str):
    num = -1
    with open('arquivo.json', 'r') as lendo:
        arquivo = json.load(lendo)
    if len(arquivo[endereco]) >= 1:
        while num != len(arquivo[endereco]):
            if arquivo[endereco][num][chave] == str(objeto):
                num = -1
                print(f'Esse {chave} já está salvo, tente novamente com outro.')
                if chave == 'codigo':
                    objeto = str(verificar_num())
                else:
                    objeto = input('Digite aqui: ')
            num += 1
    return objeto
def incluir(nome=False, cpf=False, endereco=str):
    with open('arquivo.json', 'r') as lendo:
        arquivo = json.load(lendo)
    info = {}
    print('Qual o código?')
    codigo = verificar_num()
    info['codigo'] = str(codigo)
    info['codigo'] = conferir(info['codigo'], 'codigo', endereco)
    if endereco == 'turmas':
        print('Qual o código do professor? ')
        codigo = verificar_num()
        info['professores'] = str(codigo)
        print('Qual o código da disciplina? ')
        codigo = verificar_num()
        info['disciplinas'] = str(codigo)
    if endereco == 'matriculas':
        print('Qual o código do estudante? ')
        codigo = verificar_num()
        info['estudantes'] = str(codigo)
        print('Qual o código da turma? ')
        codigo = verificar_num()
        info['turmas'] = str(codigo)
    if nome:
        info['nome'] = input('Qual o nome? ')
    if cpf:
        info['cpf'] = input('Qual o cpf? ')
        info['cpf'] = conferir(info['cpf'], 'cpf', endereco)
    info2 = info.copy()
    info.clear()  
    arquivo[endereco].append(info2)
    with open('arquivo.json', 'w') as escrevendo:
        json.dump(arquivo, escrevendo, indent=2)
def listar(endereco):
    with open('arquivo.json', 'r') as lendo:
        arquivo = json.load(lendo)
        if len(arquivo[endereco]) == 0:
            input('Não há nada nos arquivos. \nPressione ENTER para continuar.')
        else:
            for conteudo in arquivo[endereco]:
                print()
                for chave, valor in conteudo.items():
                    num = 0
                    if endereco == 'turmas' and chave == 'professores' or chave == 'disciplinas':
                        confirm = False
                        while num != len(arquivo[chave]):
                            if arquivo[chave][num]['codigo'] == str(valor):
                                nome = arquivo[chave][num]['nome']
                                print(f'{chave}: {valor} - {nome}')
                                confirm = True
                                break
                            num += 1
                        if not confirm:
                            print('Houve um engano com os códigos, por favor verifique se estão respectivamente de acordo.')
                    if endereco == 'matriculas' and chave == 'estudantes':
                        confirm = False
                        while num != len(arquivo[chave]):
                            
                            if arquivo[chave][num]['codigo'] == str(valor):
                                nome = arquivo[chave][num]['nome']
                                print(f'{chave}: {valor} - {nome}')
                                confirm = True
                                break
                            num += 1
                        if not confirm:
                            print('Houve um engano com os códigos, por favor verifique se estão respectivamente de acordo.')
                    else:
                        print(f'{chave} - {valor}')
            input('\nPressione ENTER para continuar.')
def excluir(endereco, num):
    confirm = False
    with open('arquivo.json', 'r') as lendo:
        arquivo = json.load(lendo)
        for objeto in arquivo[endereco]:
            if objeto['codigo'] == str(num):
                confirm = True
                arquivo[endereco].remove(objeto)
                break
    if confirm:
        with open('arquivo.json', 'w') as escrevendo:
            json.dump(arquivo, escrevendo, indent=2)
        input('Removido com sucesso.\nPressione ENTER para continuar.')
    else:
        input('Não encontramos esse código. Tente novamente.\nPressione ENTER para continuar.')
class editar:
    def codigo(endereco=str):
        print('Qual o código de que deseja editar?')
        cod = verificar_num()
        confirm = False
        with open('arquivo.json', 'r') as lendo:
            arquivo = json.load(lendo)
        for objeto in arquivo[endereco]:
            if objeto['codigo'] == str(cod):
                confirm = True
                print('Qual o novo código?')         
                codigo = verificar_num()
                objeto['codigo'] = str(codigo)
                objeto['codigo'] = conferir(objeto['codigo'], 'codigo', endereco)
                input('Código alterado com sucesso\nPressione ENTER para continuar.')
        if confirm:
            with open('arquivo.json', 'w') as escrevendo:
                json.dump(arquivo, escrevendo, indent=2)
        else:
            input('Não encontramos esse código. Tente novamente.\nPressione ENTER para continuar.')
    def nome(endereco=str):
        print('Qual o código de que deseja editar?')
        cod = verificar_num()
        confirm = False
        with open('arquivo.json', 'r') as lendo:
            arquivo = json.load(lendo)
        for objeto in arquivo[endereco]:
            if objeto['codigo'] == str(cod):
                confirm = True
                objeto['nome'] = input('Qual o novo nome? ')
                input('Nome alterado com sucesso\nPressione ENTER para continuar.')
        if confirm:
            with open('arquivo.json', 'w') as escrevendo:
                json.dump(arquivo, escrevendo, indent=2)
        else:
            input('Não encontramos esse código. Tente novamente.\nPressione ENTER para continuar.')
    def cpf(endereco):
        print('Qual o código de que deseja editar?')
        cod = verificar_num()
        confirm = False
        with open('arquivo.json', 'r') as lendo:
            arquivo = json.load(lendo)
        for objeto in arquivo[endereco]:
            if objeto['codigo'] == str(cod):
                confirm = True
                objeto['cpf'] = input('Qual o novo CPF? ')
                objeto['cpf'] = conferir(objeto['cpf'], 'cpf', endereco)
                input('CPF alterado com sucesso\nPressione ENTER para continuar.')
        if confirm:
            with open('arquivo.json', 'w') as escrevendo:
                json.dump(arquivo, escrevendo, indent=2)
        else:
            input('Não encontramos esse código. Tente novamente.\nPressione ENTER para continuar.')
    def tudo(endereco, cpf=True):
        print('Qual o código de que deseja editar?')
        cod = verificar_num()
        confirm = False
        with open('arquivo.json', 'r') as lendo:
            arquivo = json.load(lendo)
        for objeto in arquivo[endereco]:
            if objeto['codigo'] == str(cod):
                confirm = True
                print('Qual o novo código?')         
                codigo = verificar_num()
                objeto['codigo'] = str(codigo)
                objeto['codigo'] = conferir(objeto['codigo'], 'codigo', endereco)
                if endereco == 'turmas':
                    objeto['professores'] = input('Qual o código do novo professor? ')
                    objeto['disciplinas'] = input('Qual o código da nova disciplina? ')
                elif endereco == 'matriculas':
                    objeto['estudantes'] = input('Qual o código do novo estudante? ')
                    objeto['turmas'] = input('Qual o código da nova turma? ')
                else:
                    objeto['nome'] = input('Qual o novo nome? ')
                if cpf:
                    objeto['cpf'] = input('Qual o novo CPF? ')
                    objeto['cpf'] = conferir(objeto['cpf'], 'cpf', endereco)
                input('Alterações feitas com sucesso.\nPressione ENTER para continuar.')
        if confirm:
            with open('arquivo.json', 'w') as escrevendo:
                json.dump(arquivo, escrevendo, indent=2)
        else:
            input('Não encontramos esse código. Tente novamente.\nPressione ENTER para continuar.')
    def professor(endereco):
        print('Qual o código de que deseja editar?')
        cod = verificar_num()
        confirm = False
        with open('arquivo.json', 'r') as lendo:
            arquivo = json.load(lendo)
        for objeto in arquivo[endereco]:
            if objeto['codigo'] == str(cod):
                confirm = True
                objeto['professores'] = input('Qual o código do novo professor? ')
                break
        if confirm:
            with open('arquivo.json', 'w') as escrevendo:
                json.dump(arquivo, escrevendo, indent=2)
        else:
            input('Não encontramos esse código. Tente novamente.\nPressione ENTER para continuar.')
    def disciplina(endereco):
        print('Qual o código de que deseja editar?')
        cod = verificar_num()
        confirm = False
        with open('arquivo.json', 'r') as lendo:
            arquivo = json.load(lendo)
        for objeto in arquivo[endereco]:
            if objeto['codigo'] == str(cod):
                confirm = True
                objeto['disciplinas'] = input('Qual o código da nova disciplina? ')
                break
        if confirm:
            with open('arquivo.json', 'w') as escrevendo:
                json.dump(arquivo, escrevendo, indent=2)
        else:
            input('Não encontramos esse código. Tente novamente.\nPressione ENTER para continuar.')
    def estudante(endereco):
        print('Qual o código de que deseja editar?')
        cod = verificar_num()
        confirm = False
        with open('arquivo.json', 'r') as lendo:
            arquivo = json.load(lendo)
        for objeto in arquivo[endereco]:
            if objeto['codigo'] == str(cod):
                confirm = True
                objeto['estudantes'] = input('Qual o código do novo estudante? ')
                break
        if confirm:
            with open('arquivo.json', 'w') as escrevendo:
                json.dump(arquivo, escrevendo, indent=2)
        else:
            input('Não encontramos esse código. Tente novamente.\nPressione ENTER para continuar.')
    def turma(endereco):
        print('Qual o código de que deseja editar?')
        cod = verificar_num()
        confirm = False
        with open('arquivo.json', 'r') as lendo:
            arquivo = json.load(lendo)
        for objeto in arquivo[endereco]:
            if objeto['codigo'] == str(cod):
                confirm = True
                objeto['turmas'] = input('Qual o código da nova turma? ')
                break
        if confirm:
            with open('arquivo.json', 'w') as escrevendo:
                json.dump(arquivo, escrevendo, indent=2)
        else:
            input('Não encontramos esse código. Tente novamente.\nPressione ENTER para continuar.')
while True:
    print('\nBem vindo(a) ao Sistema, aqui gerenciamos dados.')
    print('Insira o número correspondente conforme a opção que deseja acessar.')
    print('1 - Estudantes\n2 - Professores\n3 - Disciplinas\n4 - Turmas\n5 - Matrículas\n6 - Sair do Sistema')
    opcao1 = verificar_num(1, 6)
    if opcao1 == 1:
        while True:
            print('\nEstudantes: ')
            print('1 - Incluir \n2 - Listar \n3 - Editar \n4 - Excluir \n5 - Voltar ao menu principal')
            opcao2 = verificar_num(1, 5)
            if opcao2 == 1:
                print('\nOpção de inclusão selecionada.')
                incluir(True, True, 'estudantes')
            elif opcao2 == 2:
                listar('estudantes')
            elif opcao2 == 3:
                while True:
                    print('\nOpção de edição selecionada.')
                    print('1 - Mudar o código\n2 - Mudar o nome\n3 - Mudar o CPF\n4 - Mudar tudo\n5 - Voltar ao menu estudantes')
                    opcao3 = verificar_num(1, 5)
                    if opcao3 == 1:
                        editar.codigo('estudantes')
                    if opcao3 == 2:
                        editar.nome('estudantes')
                    if opcao3 == 3:
                        editar.cpf('estudantes')
                    if opcao3 == 4:
                        editar.tudo('estudantes')
                    if opcao3 == 5:
                        break
            elif opcao2 == 4:
                print('\nOpção para excluir selecionada.')
                print('Qual o código do estudante? ')
                num = verificar_num()
                excluir('estudantes', num)
            elif opcao2 == 5:
                break
    elif opcao1 == 2:
        while True:
            print('\nProfessores: ')
            print('1 - Incluir \n2 - Listar \n3 - Editar \n4 - Excluir \n5 - Voltar ao menu principal')
            
            opcao2 = verificar_num(1, 5)
            if opcao2 == 1:
                print('\nOpção de inclusão selecionada.')
                incluir(True, True, 'professores')
            elif opcao2 == 2:
                listar('professores')
            elif opcao2 == 3:
                while True:
                    print('\nOpção de edição selecionada.')
                    print('1 - Mudar o código\n2 - Mudar o nome\n3 - Mudar o CPF\n4 - Mudar tudo\n5 - Voltar ao menu professores')
                    opcao3 = verificar_num(1, 5)
                    if opcao3 == 1:
                        editar.codigo('professores')
                    if opcao3 == 2:
                        editar.nome('professores')
                    if opcao3 == 3:
                        editar.cpf('professores')
                    if opcao3 == 4:
                        editar.tudo('professores')
                    if opcao3 == 5:
                        break
            elif opcao2 == 4:
                print('\nOpção para excluir selecionada.')
                print('Qual o código do professor? ')
                num = verificar_num()
                excluir('professores', num)
            elif opcao2 == 5:
                break
    elif opcao1 == 3:
        while True:
            print('\nDisciplinas: ')
            print('1 - Incluir \n2 - Listar \n3 - Editar \n4 - Excluir \n5 - Voltar ao menu principal')
            opcao2 = verificar_num(1, 5)
            if opcao2 == 1:

                incluir(True, False, 'disciplinas')
            elif opcao2 == 2:
                listar('disciplinas')
            elif opcao2 == 3:
                while True:
                    print('\nOpção de edição selecionada.')
                    print('1 - Mudar o código\n2 - Mudar o nome\n3 - Mudar tudo\n4 - Voltar ao menu disciplinas')
                    opcao3 = verificar_num(1, 4)
                    if opcao3 == 1:
                        editar.codigo('disciplinas')
                    if opcao3 == 2:
                        editar.nome('disciplinas')
                    if opcao3 == 3:
                        editar.tudo('disciplinas', False)
                    if opcao3 == 4:
                        break
            elif opcao2 == 4:
                print('\nOpção para excluir selecionada.')
                print('Qual o código da disciplina? ')
                num = verificar_num()
                excluir('disciplinas', num)
            elif opcao2 == 5:
                break
    elif opcao1 == 4:
        while True:
            print('Turmas: ')
            print('1 - Incluir \n2 - Listar \n3 - Editar \n4 - Excluir \n5 - Voltar ao menu principal')
            opcao2 = verificar_num(1, 5)
            if opcao2 == 1:
                incluir(False, False, 'turmas')
            elif opcao2 == 2:
                listar('turmas')
            elif opcao2 == 3:
                while True:
                    print('\nOpção de edição selecionada.')
                    print('1 - Mudar o código\n2 - Mudar o professor\n3 - Mudar a disciplina\n4 - Mudar tudo\n5 - Voltar ao menu turmas')
                    opcao3 = verificar_num(1, 5)
                    if opcao3 == 1:
                        editar.codigo('turmas')
                    if opcao3 == 2:
                        editar.professor('turmas')
                    if opcao3 == 3:
                        editar.disciplina('turmas')
                    if opcao3 == 4:
                        editar.tudo('turmas', False)
                    if opcao3 == 5:
                        break
            elif opcao2 == 4:
                print('\nOpção para excluir selecionada.')
                print('Qual o código da turma? ')
                num = verificar_num()
                excluir('turmas', num)
            elif opcao2 == 5:
                break
    elif opcao1 == 5:
        while True:
            print('Matrículas: ')
            print('1 - Incluir \n2 - Listar \n3 - Editar \n4 - Excluir \n5 - Voltar ao menu principal')
            opcao2 = verificar_num(1, 5)
            if opcao2 == 1:
                incluir(False, False, 'matriculas')
            elif opcao2 == 2:
                listar('matriculas')
            elif opcao2 == 3:
                while True:
                    print('\nOpção de edição selecionada.')
                    print('1 - Mudar o código\n2 - Mudar o estudante\n3 - Mudar a turma\n4 - Mudar tudo\n5 - Voltar ao menu matrículas')
                    opcao3 = verificar_num(1, 5)
                    if opcao3 == 1:
                        editar.codigo('matriculas')
                    if opcao3 == 2:
                        editar.estudante('matriculas')
                    if opcao3 == 3:
                        editar.turma('matriculas')
                    if opcao3 == 4:
                        editar.tudo('matriculas', False)
                    if opcao3 == 5:
                        break
            elif opcao2 == 4:
                print('\nOpção para excluir selecionada.')
                print('Qual o código da turma? ')
                num = verificar_num()
                excluir('matriculas', num)
            elif opcao2 == 5:
                break
    elif opcao1 == 6:
        break