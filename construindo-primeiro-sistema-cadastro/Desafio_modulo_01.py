''' *******************************************************************************************************
    O Objetivo: é consolidar os fundamentos de Python, transformando conceitos teóricos em um programa
                funcional que interage com o usuário, processa informações e toma decisões lógicas.
                
    O que será construido: um programa de cadastro que solicita dados pessoais, realiza operações 
    matemáticas e analisa critérios especificos (como maioridade e altura)  
    *******************************************************************************************************'''

print('********************* Fase 1 ********************')
# Fase 1 : Coleta e Armazenamento de Dados
# Entrada de dados. Deve solicitar as seguintes informações e armazená-las em variáveis com nome claros e intuitivos.
nome = input('Informe seu nome: ') # Solicita nome
idade = int(input('Informe sua idade: ') ) # Solicita idade, e deve ser um numero inteiro
altura = float(input('Informe sua altura em metros: ')) # Solicita altura e pode ser um numero decimal
ano_atual = int(input('Informe o ano atual: ')) # Solicita ano atual e deve ser um numero inteiro
print('Seu nome é:', nome ) # Imprime nome
print('Sua idade é:', idade ) # Imprime idade
print('Sua altura em metros é:', altura ) # Imprime altura
print('O ano atual é:', ano_atual ) # Imprime ano atual



print('********************* Fase 2 ********************')
# Fase 2 : Interação Personalizada
# Deve confirmar o recebimento dos dados, exibindo uma mensagem de boas vindas utlizando o nome capturado.
print('"Olá ', nome,'!', 'Seja bem-vinda ao mundo do Python"') # Imprime o nome da pessoa e uma msg de saudação



print('********************* Fase 3 ********************')
# Fase 3 : Processamento e Cálculos
# Deve descobrir o ano de nascimento
# Qtos anos a pessoa terá daqui a 5 anos
# Calular o dobro da idade 
# Calcular a idade elevada ao quadrado
ano_nascimento = int(ano_atual - idade - 1) # Calcula ano de nascimento, e deve ser inteiro. Não considera o aniversario do ano atual
idade_pos_5_anos = int(idade + 5) # Calcula idade + 5 anos, deve ser num inteiro
dobro_idade = int(idade * 2) # Calcula o dobro da idade e deve ser um num inteiro
idade_potencia_quad = int(idade ** 2) # Calcula a idade ao quadrado e deve ser um num inteiro
print('Você nasceu em:', ano_nascimento) # Imprime ano de nascimento
print('Sua idade após 5 anos: ', idade_pos_5_anos) # Imprime idade + 5 anos
print('O dobro da sua idade é:', dobro_idade) # Imprime o dobro da idade
print('Sua idade ao quadrado é:', idade_potencia_quad) # Imprime a idade ao quadrado


print('********************* Fase 4 ********************')
# Fase 4 : Lógica e Comparação
# Exibir verdadeiro ou falso para os seguintes casos:
    # Maioridade: A pessoa tem 18 anos ou mais (idade >= 18)
    # Altura minima: A altura é maior ou igual a 1.60m (altura >= 1.60)
maioridade = idade >= 18 # Validação boleana true ou false para maioridade maior ou igual a 18 anos
altura_minima = altura >= 1.60 # Validação boleana true ou false para altura maior ou igual a 1.60m
print('A pessoa tem 18 anos ou mais?', maioridade) # Imprime resultado da validação da maioridade
print('A altura é maior ou igual a 1.60m? ', altura_minima) # Imprime o resultado da validação da altura minima


print('********************* Fase 5 ********************')
# Fase 5
# Inserir comentários que documentem o codigo.
print('Inserido comentários documentando o codigo')