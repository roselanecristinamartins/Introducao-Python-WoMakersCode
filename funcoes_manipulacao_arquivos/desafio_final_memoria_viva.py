# Nesse desafio final, vamos unir o conhecimento técnico em Python com um proposito maior: registrar e preservar a memoria de mulheres 
# que marcaram a historia da tecnologia.
# Permite cadastrar, salvar, consultar e analisar informações sobre mulheres pioneiras na tech.

''' *******************************************************************************************************************
    O Objetivo: Desenvolver um programa em Python que permita cadastrar, salvar, consultar e analisar informações sobre
    mulheres pioneiras na tecnologia. Será utlizado funções, manipulação de arquivos e tratamento de erros para criar um
    sistema robusto e funcional.

    Conhecimento em pràtica:
    - Uso de variaveis e tipo de dados (str, int, float)
    - Estruturas condicionais (if, else) e de repetição (for, while)
    - Organização de dados com Listas, Tuplas e Dicionários
    - Criação de funcções para estruturar o codigo
    - Leitura e escrita de arquivos externos (.txt)
    - Tratamento de erros com try e except

    *******************************************************************************************************************'''   
import os # Importante para usar o os.path.exists

# -------------  Definição das funções ---------------------
def salvar_dados(arquivo, lista_mulheres):
    # Tenta gravar a lista de dicionários no arquivo físico, tratando erros de escrita.
    try:        
        with open(arquivo, mode='w', encoding='utf-8') as lista: # O modo 'w' cria o arquivo se ele não existir ou sobrescreve se já existir
            for m in lista_mulheres: # Percorre cada dicionário dentro da lista recebida.
                linha = f"{m['nome']};{m['area_atuacao']};{m['contribuicao']};{m['ano_periodo_historico']}\n" # Formata os dados do dicionário em uma string separada por ponto e vírgula (CSV manual)
                lista.write(linha) # Escreve a linha formatada dentro do arquivo físico      
    except PermissionError:
        print(f"❌ Erro: Sem permissão para escrever no arquivo '{arquivo}'. Verifique se ele está aberto em outro programa.")
    except Exception as e:
        print(f"❌ Erro inesperado ao salvar os dados: {e}")


def listar_historico(arquivo):
    # Tenta ler e exibir o histórico, protegendo contra arquivos corrompidos ou erros de leitura.
    if not os.path.exists(arquivo):
        print("❌ Arquivo não existe. Cadastre alguém primeiro!") # Validação de segurança: Verifica se o arquivo físico existe no disco. Se não existir, avisa o usuário e encerra a função prematuramente (Early Return)
        return
    
    try:
        print('\n--- Histórico de Mulheres Tech ---')
        with open(arquivo, mode='r', encoding='utf-8') as lista: # Abre o arquivo no modo de leitura ('r' de Read)
            for linha in lista:                
                dados = linha.strip().split(';') # O .strip() remove o '\n' (quebra de linha) do final. O .split(';') divide a string em uma lista, separando onde houver ponto e vírgula               
                if len(dados) == 4: # Garante que a linha tem os 4 campos esperados
                    print(f' Nome: {dados[0]}\n Area: {dados[1]}\n Contribuicao: {dados[2]}\n Ano: {dados[3]}\n') # Exibe os dados usando os índices da lista gerada pelo split
    
    except UnicodeDecodeError:
        print("❌ Erro de codificação: O arquivo contém caracteres que não podem ser lidos.")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado ao ler o histórico: {e}")


def exibir_estatisticas(arquivo):
    # 1. Busca e exibe informações detalhadas de uma mulher específica no arquivo.
    if not os.path.exists(arquivo): # Verificação de existência do arquivo 
        print("❌ Arquivo não existe. Cadastre alguém primeiro!")
    else:
    # Uso do try/except para capturar erros de leitura inesperados ou permissão inesperados
        try:
            nome_busca = input('Digite o Nome: ').strip().lower() # Solicita o nome, remove espaços extras (.strip) e padroniza para minúsculas (.lower)
            achou = False # Flag para controlar se a busca teve sucesso
            with open(arquivo, mode='r', encoding='utf-8') as lista:  # Abre o arquivo apenas para leitura         
                for linha in lista:
                    dados = linha.strip().split(';') # Transforma a linha do TXT em uma lista de dados separada por ';'
                    if nome_busca in dados[0].lower(): # Verificação parcial: checa se o termo buscado está dentro do nome (dados[0]). O .lower() em ambos os lados para a busca não ser "case-sensitive"
                        print(f'\n✅ Encontrada! Nome: {dados[0]} | Área: {dados[1]} | Feito: {dados[2]} | Ano: {dados[3]}') # Exibe os dados formatados usando os índices da lista
                        achou = True
            if not achou: # Se percorreu todo o arquivo e a flag 'achou' continua False, avisa o usuário
                print(f'Não existe mulher na base de dados com o nome:, {nome_busca}')
        except Exception as e: # Captura qualquer erro (ex: arquivo corrompido, erro de memória) e exibe a mensagem técnica {e}
            print(f'Ocorreu um erro inesperado: {e}')


def calcular_estatisticas(arquivo):
    # Analisa o arquivo para calcular o total de registros e os anos limite (mín/máx).   
    anos = []
    
    # 1. Tentativa de abrir o arquivo para leitura
    try:
        with open(arquivo, mode='r', encoding='utf-8') as lista:            
            todas_as_linhas = lista.readlines() # .readlines() lê o arquivo inteiro e gera uma lista de strings (uma por linha)
            total_mulheres_cad = len(todas_as_linhas)        
       
            for linha in todas_as_linhas: # Percorre a lista gerada para extrair apenas o campo 'ano'
                dados = linha.strip().split(';')               
                anos.append(int(dados[3]))  # Convertemos para int para que as funções min() e max() funcionem numericamente
        
        # 2. Verificação: Se a lista 'anos' não estiver vazia, exibe os cálculos
        if anos:
            mais_antigo = min(anos)
            mais_recente = max(anos)
            print(f'\n📊 Estatísticas de Período:')
            print(f'📊 Total de mulheres Tech cadastradas: {total_mulheres_cad}')
            print(f'📅 O ano mais antigo registrado foi em: {mais_antigo}')
            print(f'📅 O ano mais recente registrado foi em: {mais_recente}')
        else:
            print('⚠️ Nenhum dado cadastrado para calcular estatísticas.')

    # 3. Tratamento de erro caso o arquivo físico ainda não tenha sido criado
    except FileNotFoundError:
        print('❌ Arquivo não existe. Faça um cadastro primeiro!')
    except Exception as e:
        print(f'❌ Erro ao processar estatísticas: {e}')

# ----------- Código principal -----------

# Configurações iniciais: nome do arquivo físico e inicialização da lista na memória (RAM) 
arquivo = 'memoria_mulheres_tech.txt'
mulheres_tech = []
opcao = None

while opcao != 5:  # Loop principal: o programa rodará repetidamente até que a opção 5 (Sair) seja escolhida
    print('\n MENU DE OPÇÕES \n1 - Cadastrar Mulher Tech \n2 - Listar Histórico \n3 - Buscar por Nome \n4 - Exibir estatíticas \n5 - Sair')
    
    try: 
        opcao = int(input('\n Digite a opção desejada: ')) # Tenta converter a entrada do usuário para inteiro. Se falhar, vai direto para o 'except'.
            
        # Opção 1: Coleta de dados e salvamento
        if opcao == 1: 
            nome = input('Nome: ')
            area_atuacao = input('Area de atuação: ')
            contribuicao = input('Contribuição ou feito mais relevante: ')
            ano_periodo_historico = input('Ano ou periodo histórico: ')

            # Cria um dicionário e o adiciona à lista temporária 'mulheres_tech'
            mulheres_tech.append({'nome': nome, 'area_atuacao': area_atuacao, 'contribuicao': contribuicao, 'ano_periodo_historico': ano_periodo_historico})

            # Persistência de Dados: Chama a função que grava a lista atualizada no arquivo TXT
            salvar_dados(arquivo, mulheres_tech) 
            print(f'✅ {nome} Adicionada com sucesso!')
                
        
        # Opção 2: Exibir todos os registros salvos
        elif opcao == 2: 
            # Chama a função de leitura, passando o nome do arquivo definido no início
            # Esta função vai abrir o arquivo, ler linha por linha e formatar o texto para o usuário
            listar_historico(arquivo) # Chamada da função

        
        # Opção 3: Filtrar e encontrar uma mulher específica
        elif opcao == 3:
            # Chama a função de busca detalhada. 
            # Lá dentro, o programa vai pedir o nome, abrir o arquivo e tentar encontrar a correspondência.
            exibir_estatisticas(arquivo)


        # Opção 4: Analisa o arquivo para calcular os registros e os anos + recentes e + antigo.
        elif opcao == 4:
           # Chama a função de estatistica
           # Analisa o arquivo para calcular o total de registros e os anos limite (mín/máx).
            calcular_estatisticas(arquivo)          

        
        # Opção 5: Finalização do programa com mensagem inspiradora
        elif opcao == 5:
            print('Saindo do programa')
            # Frase de impacto para encerrar a experiência do usuário
            print('Este arquivo existe porque histórias importam. Mulheres sempre estiveram presentes na tecnologia. E agora, você também faz parte dessa transformação!')       
        else: # Tratamento de erro: Caso o usuário digite um número que não está no menu
            print('❌ Opção inexistente. Por favor, escolha um número entre 1 e 5.')          

    
    # Tratamento de erro específico para entradas que não são números inteiros
    except ValueError: 
        # Se o usuário digitar "abc" ou deixar vazio, o Python não 'quebra'; 
        # ele desvia para cá e exibe este aviso.
        print('❌ Entrada inválida. Por favor, digite apenas números!')

