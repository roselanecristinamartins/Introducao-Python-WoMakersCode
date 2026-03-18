''' ********************************************************************************************************************************************
    O Objetivo: é criar um Menu Interativo. O diferencial é que o programa não vai apenas rodar e fechar; ele
                deve continuar 'vivo' e disponivel para o usuário até que ela decida encerrar a navegação.
                Para isso, deve ser utilizado o WHILE. Se a condição for verdadeira, o codigo é executado mais
                uma vez, senão o programa é encerrado.
  

    Menu de opções - Requisitos:
        1- Estrutura de repetição: usar while para manter o menu ativo
        2- Variável controle: crie uma variável, ex: opção, para armazenar a escolha do user e definir qdo o ciclo deve parar.
        3- Sitema de contagem: Crie um contador para registrar qtas vezes o menu foi exibido ou qtas interações foram feitas durante a execução
        4- Interação e escolha: O programa deve processar as seguintes informações
            Opção 1: Exibe uma mensagem de boas-vindas personalizada
            Opção 2: Informa o valor atual do seu contador
            Opção 3: Encerra o programa com uma mensagem de despedida 
        5- Desafio extra: 
            Tratamento de erro: Exibir uma mensagem caso o user digite um numero que não está no menu.
            Pesonalização: Pergunte o nome do user logo no início e use-o nas mensagens do sistema.

    ********************************************************************************************************************************************'''

contador = 0
opcao = None
nome = str(input('Informa seu nome: ')) # Desafio extra - personalização
while opcao != 3: # Será mantido ativo até que seja digitado '3'
    contador += 1  # Contador que registra quantas vezes o menu foi exibido
    print('1- Mostra msg personalizada') # Opções do menu
    print('2- Mostra valor atual do contador') # Opções do menu
    print('3- Mostra msg de despedida') # Opções do menu
    opcao = int(input('Escolha uma opção: ')) # Pede pra escolher uma opção do menu
    if opcao == 1:
        print('Bem vinda ao sistema', nome) # Mensagem de saudação + nome do usuário
    elif opcao == 2:
        print(nome, ', o valor do contador é: ', contador) # Mostra quantas vezes o menu foi exibido
    elif opcao == 3:
        print('Obrigada pela participação ', nome) # Encerra o programa
    elif opcao > 3 or opcao < 1: # Desafio extra  - tratamento de erro
        print('Opção não existe no menu, escolha uma opção válida ', nome)

      

