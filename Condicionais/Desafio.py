

# - ***Desafio 1 Condicionais***

# ***Crie um sistema de e-commerce, onde o usuário possa:***

# *Utilize variáveis, listas, condicionais*

# Foco resolver o problema

# Vamos trabalhar:

# ***Criatividade | Pensamento lógico | Flexibilidade cognitiva***

# - ***cadastrar-se***
# - ***comprar um produto***
# - ***descobrir o valor total***
# - ***pagar***



print('                                            ')
print('-----------E-commercer------------- ')

print(''' 
        |  Cadastre-se  |
         ---------------          ''')

nome = str(input('Digite seu Nome: '))
idade = int(input('Digite sua Idade: '))
Email = str(input('Digite o E-mail: '))
senha = int(input('Digite sua senha: '))  

print('                                     ')
print('                                     ')
print(f'{nome}, Seja bem-vindo! Cadastro realizado com sucesso!')
print('                                                       ')
print('Deseja continuar para acessar nossos produtos: Opções 1 Sim ♥ --> 2 Não')

op = int(input())

if op == 1:
    print('Nossos produtos listados abaixo:')
elif op == 2:
    print('Obrigado pelo cadastro!')
    exit() 
else:
    print('Opção inválida!')
    exit() 



print('''
Escolha um produto a partir do Código do produto:
0 - books
1 - Manuais e apostilas
2 - Infográficos
3 - Softwares
4 - Podcasts
''')

carrinho_prod = ['books', 'Manuais e apostilas', 'Infográficos', 'Softwares', 'Podcasts']
carrinho_valores = [20.50, 15.00, 25.00, 150.00, 10.00]


opcao = int(input('Digite o ID do Produto: '))


if opcao < 0 or opcao >= len(carrinho_prod):
    print('Código inválido')
    exit()

compra = []
total = 0.0


compra.append(carrinho_prod[opcao])
total += carrinho_valores[opcao]


print('-------------------'*2)
print(f'Produto - {carrinho_prod[opcao]} valor R$ {carrinho_valores[opcao]:.2f}')

print(f'Total - R$ {total:.2f}')


forma_de_pagamento = {
    1: "PIX",
    2: "Débito",
    3: "DINHEIRO"
}

print('''
Forma de pagamento:
1: PIX
2: Débito
3: DINHEIRO
''')

escolha_fr_pag = int(input('Escolha a forma de pagamento: 1 PIX, 2 Débito, 3 DINHEIRO: '))


if escolha_fr_pag == 1:
    form = forma_de_pagamento[1]
    print(f'Seu pagamento será efetuado via {form}')

elif escolha_fr_pag == 2:
    form = forma_de_pagamento[2]
    print(f'Seu pagamento será efetuado via {form}')  
elif escolha_fr_pag == 3:

    form = forma_de_pagamento[3]
    print(f'Seu pagamento será efetuado via {form}')
    
else:
    print('Opção de pagamento inválida! Tente novamente.')
print('   '*10)




# dados = {}


# usuario_nome  =  input('Digite seu nome:')
# usuario_login = input('Digite o login')
# usuario_senha = input('Digite sua senha')


# dados['nome'] = usuario_nome
# dados['login'] = usuario_login
# dados['senha'] = usuario_senha


# senha_acess = input('Digite a senha')
# if dados['senha'] == senha_acess:
#     carrinho = []
#     meu_total = []
#     prod = ['IPHONE','DELL', 'MESA DE PC', 'FONE'] 
#     valores = [10.45,20.25,35.00,50.00]
#     print('Escolha o produto pelo ID - 0 - 1 - 2 - 3', prod)
#     escolha_produto1 = int(input('Escolha:'))
#     escolha_produto2 = int(input('Escolha:'))
#     carrinho.append(prod[escolha_produto1])
#     carrinho.append(prod[escolha_produto2])
#     meu_total.append(valores[escolha_produto1])
#     meu_total.append(valores[escolha_produto2])
#     print('Seus produtos', carrinho)
    
#     print('>>>>'*10)
#     soma  =sum( meu_total)
#     print('Total do pedido R$', soma)
# else:
#     print('Acesso negado, senha incorreta') 