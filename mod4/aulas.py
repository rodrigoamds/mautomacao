import os

print(f'Diretório atual: {os.getcwd()}')

print('#4.2: Trocando para pasta "desafio arquivos"...')
os.chdir('desafio arquivos')

print(f'Diretório atual: {os.getcwd()}')
conteudo_pasta = os.listdir()
print(f'#1: Conteúdo da pasta: {conteudo_pasta}')
print('#2: Path completa dos arquivos:')
for elemento in conteudo_pasta:
  if '.' in elemento:
    print(os.path.join(os.getcwd() + os.sep + elemento ))

os.chdir('desafio texto')
print('#4.1: Trocando para pasta "desafio texto"...')

conteudo_pasta = os.listdir()
print('#3: Path completa dos arquivos:')
for elemento in conteudo_pasta:
  if '.' in elemento:
    print(os.path.join(os.getcwd() + os.sep + elemento ))

print(f'Diretório atual: {os.getcwd()}')

os.chdir('..')
print(f'Diretório atual: {os.getcwd()}')
os.chdir('..')
print(f'#4.3: Diretório atual: {os.getcwd()}')