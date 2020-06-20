import random
import time

class Questao:
    
    def Iniciar(self):
        print('Jogando...')
        time.sleep(random.randint(3,6))
        self.Responder()
        
    def Responder(self):
        resposta = random.randint(1,6)
        print(resposta)
        
pergunta_inicial = input('Vamos jodar o dado? (s/n): ')     

c = 0
while pergunta_inicial == 's':
  questao = Questao()
  questao.Iniciar()
  c += 1
  if c > 0:
    pergunta_inicial = input('Vamos continuar? (s/n)')     

print(f'Até a próxima. Você jogou {c} vezes')