from sqlalchemy import Column, Integer,  String, DateTime, Numeric, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from models.base import base


class Artista(base):
    __tablename__ = 'artista'
    artista_id = Column(Integer, Sequence(
        'artista_id_auto_incremento', start=1), primary_key=True)
    nome = Column(String)
    albuns = relationship('Album')


class Album(base):
    __tablename__ = 'album'
    album_id = Column(Integer, Sequence(
        'album_id_auto_incremento', start=1), primary_key=True)
    titulo = Column(String)
    # 12345678.50 total de 10 números com precisão máxima de 2 ponto decimais # signfica que não posso colocar números maiores que isso? Não, isso significa que você perde precisão
    preco = Column(Numeric(precision=10, scale=2))
    artista_id = Column(Integer, ForeignKey('artista.artista_id'))
    cancoes = relationship('Cancao')
    estilo = relationship('EstiloMusical')


class Cancao(base):
    __tablename__ = 'cancao'
    cancao_id = Column(Integer, Sequence(
        'cancao_id_auto_incremento', start=1), primary_key=True)
    nome = Column(String)
    album_id = Column(Integer, ForeignKey('album.album_id'))


class EstiloMusical(base):
    __tablename__ = 'estilo'
    estilo_id = Column(Integer, Sequence(
        'estilo_id_auto_incremento', start=1), primary_key=True)
    nome = Column(String)
    album_id = Column(Integer, ForeignKey('album.album_id'))
