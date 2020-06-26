import random
import time

class Questao:
    def __init__(self):
        self.resposta = random.randint(1,100)
        self.tentativas = 0
        self.chute = 0
        
    def PegaValor(self, frase):
      try:
        self.chute = int(input(frase))
        self.tentativas += 1
      except ValueError:
        print('Digite apenas números')
        self.PegaValor(frase)

    def Resolver(self):
        if self.tentativas == 0:
          self.PegaValor('Chute um valor entre 1 e 100: ')

        while self.chute != self.resposta:
          if(self.chute < self.resposta):
            self.PegaValor('Chute para cima: ')
            #self.tentativas += 1
          else:
            self.PegaValor('Chute para baixo: ')
            #self.tentativas += 1          

        print(f'Parabéns, levou {self.tentativas} tentativas para acertar')

    
questao = Questao()
questao.Resolver()
