import sqlalchemy
from sqlalchemy import create_engine, Column, Integer,  String, DateTime, Numeric, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

base = declarative_base()


class Artista(base):
    __tablename__ = 'artista'
    artista_id = Column(Integer, Sequence('artista_id_auto_incremento', start=1), primary_key=True)
    nome = Column(String)
    albuns = relationship('Album')


class Album(base):
    __tablename__ = 'album'
    album_id = Column(Integer, Sequence('album_id_auto_incremento', start=1), primary_key=True)
    titulo = Column(String)
    # 12345678.50 total de 10 números com precisão máxima de 2 ponto decimais # signfica que não posso colocar números maiores que isso? Não, isso significa que você perde precisão
    preco = Column(Numeric(precision=10, scale=2))
    artista_id = Column(Integer, ForeignKey('artista.artista_id'))
    estilo_id = Column(Integer, ForeignKey('estilo.estilo_id'))
    cancoes = relationship('Cancao')


class Cancao(base):
    __tablename__ = 'cancao'
    cancao_id = Column(Integer, Sequence('cancao_id_auto_incremento', start=1), primary_key=True)
    nome = Column(String)
    album_id = Column(Integer, ForeignKey('album.album_id'))


class EstiloMusical(base):
    __tablename__ = 'estilo'
    estilo_id = Column(Integer, Sequence(
        'estilo_id_auto_incremento', start=1), primary_key=True)
    nome = Column(String)
    album_id = Column(Integer, ForeignKey('album.album_id'))


engine = create_engine('sqlite:///artistas.db', echo=True)
base.metadata.drop_all(bind=engine)  # Dropa estrutura atual
base.metadata.create_all(bind=engine)  # Cria tabelas baseados na


Conexao = sessionmaker(bind=engine)
conexao = Conexao()



novo_artista1 = Artista()
novo_artista1.nome = 'Jhonatan Dev'

novo_artista2 = Artista()
novo_artista2.nome = 'Jeff Bezos'

album1 = Album()
album1.titulo = 'Album 1'
album1.preco = 12.01
album1.artista_id = 1

album2 = Album()
album2.titulo = 'Album 2'
album2.preco = 14.01
album2.artista_id = 1

album3 = Album()
album3.titulo = 'Album 3'
album3.preco = 15.05
album3.artista_id = 1

album4 = Album()
album4.titulo = 'Album 4'
album4.preco = 50.55
album4.artista_id = 2

album5 = Album()
album5.titulo = 'Album 5'
album5.preco = 25.25
album5.artista_id = 2

album5 = Album()
album5.titulo = 'Album Top! 5'
album5.preco = 25.25
album5.artista_id = 2

conexao.add(novo_artista1)
conexao.add(novo_artista2)
conexao.add(album1)
conexao.add(album2)
conexao.add(album3)
conexao.add(album4)
conexao.add(album5)

conexao.commit()
# Obter tudo registrado em uma tabela
for item in conexao.query(Artista).all():
    print(item.artista_id, item.nome)
# Obter a quantidade de registros em uma tabela
print(conexao.query(Artista).count())
# Obter o primeiro registro em uma tabela
artista = conexao.query(Artista).first()
print(artista.artista_id, artista.nome)
# Obter resultados ordenados baseado em alguma condição
for item in conexao.query(Artista).order_by(Artista.artista_id):
    print(item.nome, item.artista_id)
# Obter apenas uma quantidade de resultados específica
for item in conexao.query(Album).limit(3):
    print(item.album_id, item.titulo)
# Filtrar por propriedades específicas
for item in conexao.query(Album).filter(Album.artista_id == 2).\
        filter(Album.preco == 25.25):
    print(item.titulo, item.album_id)
# Pesquisando por itens que contem um string
for item in conexao.query(Album).filter(Album.titulo.like('%top%')):
    print(item.titulo, item.album_id)


# Desafio - Vou deixar o código dessa aula em anexo, eu quero que você baixe ela instale as dependências e adicone 3 albuns e 2 artistas a seguir e depois encontre as seguintes informações:
#  a Resposta deste desafio estará na próxima aula. Caso encontre algum erro, em função de sistemas operacionais diferentes, não entre em pânico. Pegue o erro, jogue no google e tente encontrar uma solução. Se mesmo assim não conseguir resolver, poste sua dúvida aqui dizendo o que já tentou, que iremos tentar te ajudarr. Para que você consiga fazer o desafio, você deve usar exatamente o que vou te passar aqui, se passar dados diferentes nossos resutlados não irão bater
'''
Adicone um novo artista chamado
nome: 'Novo Artista'
Adicone um novo artista chamado
nome: 'Novo Artista 2'

Adicione o album
titulo: 'Summer 3000'
preco: 10
artista_id: 3
Adicione o album
titulo: 'Winter Times'
preco: 25
artista_id: 4
Adicione o album
titulo: 'Sunny Morning'
preco: 35
artista_id: 4
'''
# Feito isso encontre e exiba na tela as seguintes informações:
'''
1 - Exiba a quantidade de albuns que estão cadastrados atualmente no banco de dados
2 - Exiba todos os artisitas que possuem a palavra "novo" no nome
3 - Exiba todos os albuns criados pelo artista "Novo Artista 2"
4 - Exiba o id e título de todos os álbuns que possuem um preço abaixo de 30 
'''