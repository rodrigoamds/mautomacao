# nome_pessoa = input('Seu nome')

# if nome_pessoa == 'josé':
#   print("Pode entrar")
# elif nome_pessoa == 'marcos':
#   print("Pode entrar")
# elif nome_pessoa == 'camilla':
#   print("Pode entrar")
# else : print("Vaza")

# lista = ['rodrigo', 'tati', 'paul']

# for item in lista:
#   print(item)

# for passo in range(1,11):
#   print(f'Executando passo {passo}')

# preco_celular = 1000
# while preco_celular >= 800.0:
#   preco_celular = float(input('Qual o preço? '))
#   print('Caaaaarooo demaaais, continue procurando')
# print(f'Preço bacaninha encontrado: {preco_celular}')

# lista = [5, 10,20,30,40]

# for preco in lista:
#   print(f'Valor atual {preco}')
#   if preco == 20:
#     print('            ^ Preço localizado')
#     break

# sites = ['google', 'face', 'insta']
# for site in sites:
#   if site == 'face':
#     print(f'{site} foi pulado')
#     continue
#   print(f'Site atual: {site}')



for cont in range(10):
  try:
    print(5/0)
  except:
    print('deu erro')