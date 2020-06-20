import random
import time

class Questao:
    def __init__(self):
        self.respostas = ['Sei lá', 'Estou com sono', 'Mais tarde talvez', 'Vamos ver', 'Creio que não','Amanhã pode ser']
    
    def Iniciar(self):
        input('Faça sua pergunta: ') # inicie o debug aqui (coloque um breakpoint)
        print('Deixa eu pensar...') # Para a execução aqui novamente usando um break point
        time.sleep(random.randint(3,6))
        self.Responder()
        
    def Responder(self):
        resposta = random.choice(self.respostas)
        print(resposta)
        
pergunta_inicial = input('Vamos lá? (s/n): ')     

c = 0
while pergunta_inicial == 's':
  questao = Questao()
  questao.Iniciar()
  c += 1
  if c > 0:
    pergunta_inicial = input('Vamos continuar? (s/n)')     

print(f'Até a próxima. Você fez {c} perguntas')