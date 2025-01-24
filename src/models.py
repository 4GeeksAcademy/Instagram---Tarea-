import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    # id = Column(Integer, primary_key=True)
    # user_from_id = Column(String(250), nullable=False)
    # user_to_id = Column(String(250), nullable=False)
    # variable1 = relationship("variable1", back_populates="usuario", uselist=False)  # Relación uno a uno

    id = Column(Integer, primary_key=True)  # ID único de cada relación
    user_from_id = Column(Integer, ForeignKey('usuario.id') nullable=False)  # Usuario que sigue
    user_to_id = Column(Integer, ForeignKey('usuario.id') nullable=False)  # Usuario seguido


class Usuario(Base):
    __tablename__ = 'usuario'
    # # Here we define columns for the table address.
    # # Notice that each column is also a normal Python instance attribute.
    # id = Column(Integer, primary_key=True)
    # username = Column(String(250))
    # firstname = Column(String(250))
    # lastname = Column(String(250), nullable=False)
    # email = Column(String(250), nullable=False)
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Follower)
    # # conectando comentarios con usuarios
    # comments = relationship("Comment", back_populates="user")  # Relación uno a muchos
    id = Column(Integer, primary_key=True)  # ID único del usuario
    username = Column(String(250))  
    firstname = Column(String(250))  
    lastname = Column(String(250), nullable=False)  # Apellido
    email = Column(String(250), nullable=False)  # Correo electrónico
    comments = relationship("Comment", back_populates="user")  # Relación con la tabla Comment
    usuario_from_id = relationship("Follower", back_populates="follower")
    user_to_id = relationship("Follower", back_populates = "user")

class Comment(Base):
    __tablename__ = 'comment'
   
    # id = Column(Integer, primary_key=True)
    # comment_text = Column(String(250), nullable=False)
    # author_id = Column(Integer, ForeignKey('author.id'),nullable=False)
    # post_id = Column(Integer, nullable=False)
    # user = relationship("user", back_populates="comment")  # Relación uno a muchos
    id = Column(Integer, primary_key=True)  
    comment_text = Column(String(250), nullable=False)  
    author_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)  # ID del usuario que comentó
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)  # ID del post comentado
    user = relationship("Usuario", back_populates="comments")  # Relación con el usuario



class Post(Base):
    __tablename__ = 'post'
   
    # id = Column(Integer, primary_key=True)
    # user_id = Column(Integer, nullable=False) 
    # post_id = Column(Integer, ForeignKey('post.id'))
    # person = relationship("person", back_populates="Media")
    id = Column(Integer, primary_key=True)  
    user_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)  # ID del usuario que creó el post
    comments = relationship("Comment", back_populates="post")  # Relación con los comentarios
    
    


class Media(Base):
    __tablename__ = 'media'
   
    # id = Column(Integer, primary_key=True)
    # type = Column(Enum(StatusEnum), nullable=False)
    # url = Column(String(250), nullable=False)
    # post_id = Column(Integer, nullable=False)
    # relacionconpost = relationship("relacionconpost", back_populates="post", uselist=False)  # Relación uno a uno
    id = Column(Integer, primary_key=True)  
    type = Column(String(250), nullable=False) 
    url = Column(String(250), nullable=False)  
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)  


    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
