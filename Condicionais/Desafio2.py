
# # Cada cliente deve escolher um quarto para sua estadia.
# # O preço da diária varia conforme o tipo de quarto:
# # Simples: R$ 100,00 por dia.
# # Duplo: R$ 150,00 por dia.
# # Luxo: R$ 250,00 por dia.


# testando "For" da aula 09 

QUARTOS = ['SIMPLES','DUPLO', 'LUXO']
PRECOS = [100, 150, 250]

def calcular_valor(total_dias, tipo_quarto):
    
    return total_dias * PRECOS[tipo_quarto]

def mostrar_opcoes_quarto():
    
    print("Escolha o tipo de quarto:")
    for i, quarto in enumerate(QUARTOS):
        print(f"{i} - {quarto}")

def obter_quarto():
    
    while True:
        try:
            quarto = int(input("Digite o número do quarto escolhido (0, 1 ou 2): "))
            if 0 <= quarto <= 2:
                return quarto
            else:
                print("Opção inválida! Escolha um número entre 0 e 2.")
        except ValueError:
            print("Por favor, insira um número válido.")

def obter_dias():
    
    while True:
        try:
            dias = int(input("Digite a quantidade de dias de estadia: "))
            if dias > 0:
                return dias
            else:
                print("Por favor, insira um número positivo para os dias.")
        except ValueError:
            print("Por favor, insira um número válido.")

clientes = 3
for i in range(1, clientes + 1):
    print(f"\nCliente {i}:")
    
    
    mostrar_opcoes_quarto()
    tipo_quarto = obter_quarto()
    print(f"Quarto escolhido: {QUARTOS[tipo_quarto]}")
    
    
    dias = obter_dias()
    
   
    total = calcular_valor(dias, tipo_quarto)
    print(f"Valor total para {dias} dias no quarto {QUARTOS[tipo_quarto]}: R$ {total:.2f}")





# cliente_nome1 = input('Nome:  ')
# cliente_idade1 = int(input('Idade: ')) 
# cliente_nome2 = input('Nome:  ')
# cliente_idade2 = int(input('Idade: ')) 


# lista_quartos =  ['SIMPLES', 'DUPLO', 'LUXO']
# lista_valores_quartos = [100.0,150.0,250.0]


# print('escolha a partir do código do quarto 0 - 1 - 2  ', lista_quartos)


# escolha_quarto1 = int(input('Escolha o quarto Cliente 1: '))
# escolha_quarto2 = int(input('Escolha o quarto Cliente 2: ')) 


# dias_quat1 = int(input(f'Digite os dias {cliente_nome1}'))
# dias_quat2 = int(input(f'Digite os dias {cliente_nome2}'))


# calc1 = lista_valores_quartos[escolha_quarto1] * dias_quat1
# calc2 = lista_valores_quartos[escolha_quarto2] * dias_quat2


# print('O Usuário ', cliente_nome1, 'escolheu o quarto',lista_quartos[escolha_quarto1])
# print('O Usuário ', cliente_nome2, 'escolheu o quarto',lista_quartos[escolha_quarto2])


# print('Total cliente',cliente_nome1, 'R$', calc1)
# print('Total cliente',cliente_nome2, 'R$', calc2)