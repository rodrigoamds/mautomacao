class EmailDeBoasVindas:
    def __init__(self):
        self.pessoas = ['Cristian','Robert','Rossana','Ana']
    
    def Iniciar(self):
      emails_apresentacao = self.MontarCredencial(self.pessoas)
      for email in emails_apresentacao:
        print(email)
        print(emails_apresentacao[3])


    def MontarCredencial(self, pessoas):
        credenciais = []
        for pessoa in pessoas:
            credenciais.append(f'A empresa gostaria de dar as boas vindas para o(a) {pessoa}')
        return credenciais

email = EmailDeBoasVindas()
email.Iniciar()

# Desafio
import random
class EmailDeBoasVindas:
    def __init__(self):
        self.pessoas = ['Cristian','Robert','Rossana','Ana']
    
    def Iniciar(self):
        print('Olá bem vindo a este site!') # inicie o debug aqui (coloque um breakpoint)
        self.ChutarIdade(self.pessoas) # Pule essa linha
        self.ChutarNome() # Entre dentro do método dessa linha
        self.ChutarCor() # Entre neste método
        print('Programa finalizado') # Para a execução aqui novamente usando um break point
        
        
    def ChutarCor(self):
        cores = ['azul','rosa','verde',]
        for cor in cores:
            print(f'as opções de cores são: {cor}')
        
        print('sua cor favorita é...') # não continue a execução aqui, volte para onde estava antes
        cor_preferida = random.choice(cores)
        print(cor_preferida)

    def ChutarNome(self):
        nome = f'bem vindo {random.choice(self.pessoas)}'
        print(nome)

    def ChutarIdade(self, pessoas):
        # Entre aqui
        idade = random.randint(18,50)
        print(idade)

email = EmailDeBoasVindas()
email.Iniciar()