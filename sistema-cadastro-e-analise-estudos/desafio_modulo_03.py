''' *******************************************************************************************************************
    O Objetivo: construir um programa que organiza informações de participantes de um curso e gere pequenos relatórios
                de desempenho. Aqui veremos como listas, dicionários e laços de repetição trabalham em equipe! 

    *******************************************************************************************************************'''           
                
# Dados fixos (Tuplas)
# Existem informações que não devem ser alteradas por acidente, por isso usaremos tuplas.
dados_curso = ('Python para iniciantes |', 'Duração: 1 mês |', 'Carga horária: 60h') # Tupla
print(f'Curso: {dados_curso[0]}  Tempo: {dados_curso[1]}  Carga horária: {dados_curso[2]}')


# Cadastro estruturado (Lista + dic)
participante = [] # Criação de lista para armazenamento dos dicionários

# Menu interativo (while) 
# O menu deve ficar ativo até pressionar 5.
opcao = None
while opcao != 5:
    print('\n MENU DE OPÇÕES \n1 - Cadastrar participante \n2 - Mostrar participantes \n3 - Ver análises \n4 - Exibir lista de areas de interesse \n5 - Sair') # Mostra as opções do menu
    opcao = int(input('\n Escolha uma opção: ')) # Interage com usuáerio pedindo pra digitar uma opção do menu

    # Ocorre a execução da rotina associada a opção escolhida no menu
    # Opção 1: Cadastra participante
    if opcao == 1: 
        nome = input('Nome: ') # Pede nome
        while True: # Laço que valida idade
            idade = int(input('Idade: '))
            if idade >= 0: 
                break # sai se estiver correto
            print('❌ Erro: A idade não pode ser negativa. Tente de novo.') # Printa erro, caso a idade seja negativa

        while True: # Laço que valida horas de estudo
            horas = int(input('Horas de estudo: '))
            if horas >= 0:
                break
            print('❌ Erro: As horas não podem ser negativas. Tente de novo.')  # Printa erro, caso a hora seja negativa    
        area = input('Área: ') # Pede area de interesse
        
        # Cada participante será representado por um dicionário, contendo nome, idade, horas_estudo e area_interesse. Para não 
        # perder os dados, cada dicionário criado deve ser armazenado dentro de uma lista glbal de participantes
        novo_participante = {'nome': nome, 'idade': idade, 'horas_estudo': horas, 'area_interesse': area} # Estrutura os dados capturados em um dicionário
        participante.append(novo_participante) # Armazena o dicionário na lista global para persistência em memória
        print(f'✅ {nome} Adicionada com sucesso!')  

    # Opção 2: Mostra participante
    elif opcao == 2: 
        total_participantes = len(participante)  # Guarda a quandidade de participantes
        print('\n--- Lista de participantes cadastradas ---') 
        for p in sorted(participante, key=lambda x: x['nome']): 
            print(f"Nome: {p['nome']} | Área: {p['area_interesse']}") # Printa lista de participante e area de interesse
        print('Total de alunas cadastrada', total_participantes) # Printa total de participantes
            
    # Opção 3: Mostrar análises
    elif opcao == 3: 
        total_participantes = len(participante)         

        if total_participantes > 0:
            total_horas = sum(aluna['horas_estudo'] for aluna in participante)
            media_horas_gp = total_horas / total_participantes   # Faz a mádia das horas de estudo dos participantes

            maior_idade = 0            
            alunas_destaque = []  # Cria lista vazia pra guardar os nomes de destaque
            
            # print(f"\n--- ANÁLISE DO TOTAL DE {total_participantes} PARTICIPANTES ---") # Printa cabeçalho para análise dos dados
            
            for i in participante: # Itera sobre a coleção de participantes add novos dados (idade_dobro, idade_quadrado)
                i['idade_dobro'] = i['idade'] * 2 # Calcula e injeta o dobro da idade como um novo atributo do dicionário
                i['idade_quadrado'] = i['idade'] ** 2 # Calcula e injeta a idade ao quadrado utilizando o operador de potência (**)
            print(participante)
            
            
            for aluna in participante:                
                if aluna['idade'] >= 16: # Logica de contagem Maior de idade
                    maior_idade += 1 
                print(f"\n>> Aluna: {aluna['nome']} | Idade: {aluna['idade']}") 

                
                if aluna['horas_estudo'] >= 5: # Melhor aproveitamento
                    alunas_destaque.append(aluna['nome'])   # Guarda aluna com bom tempo de estudo
                    print(f'  ✨ Bom ritmo de estudo: {aluna["horas_estudo"]}h') 
                else:
                    print(f'  ❌ Não possui bom ritmo de estudo: {aluna["horas_estudo"]}h')
                                  
                
                if aluna['idade'] >= 16 and aluna['horas_estudo'] >= 5: # Validação do requisito básico
                    print('  ✅ Status: Atende aos requisitos basicos de idade e bom ritmo')
                else:
                    print('  ❌ Status: Não cumpre os requisitos') 

            # Exibe os totais após termino do loop
            print(f'\n📊 ANÁLISE DE DADOS:')
            print('Total participantes', total_participantes)            
            print('Quantidade de alunas maiores de idade: ', maior_idade)
            print('A media de horas de estudo do grupo :', media_horas_gp)
            
            if alunas_destaque: # Verifica se existem registros na lista de destaque antes de exibir
                print(f'✨ Alunas com bom ritmo (>= 5h): {", ".join(alunas_destaque)}') # Formata a lista de nomes em uma única string separada por vírgulas
            else:
                print(f'  ⚠️ Sem alunas com bom ritmo no momento') # Feedback visual para o usuário caso o critério de destaque não tenha sido atingido
            
        else:
            print('Nenhum dado para mostrar.') # Caso não existam dados para analisar
    
    # Opção 4: Exibir lista de area de interesse sem repetir nomes
    elif opcao == 4:
        if not participante:
            print('⚠️  Nenhum cadastro encontrado!')
        else:
            lista_areas = []
            for aluna in participante:
                area = aluna['area_interesse']
                if area not in lista_areas: # Valida se area não esta na lista, e se não estiver apenda
                    lista_areas.append(area)

            print(f' Área de interesse cadastradas')
            for area in lista_areas:
                print(f'  • {area}') # Printa areas

    # Opção 5: Saida do menu
    elif opcao == 5:
        print('Finalizado')
        break

    elif opcao > 5 or opcao < 1: # Tratamento de erro
        print('Opção não existe no menu, escolha uma opção válida ')