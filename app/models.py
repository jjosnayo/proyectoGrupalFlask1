from app import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref


class Usuario(db.Model):
    __tablename__ = "Usuario"
    name = db.Column(db.String(80), nullable=False)  # nombre real
    phone = db.Column(db.String(9), nullable=False)  # 9 digitos
    adress = db.Column(db.String(120), nullable=False)  # direccion tienda fisica
    # info para el register
    username = db.Column(db.String(80), primary_key=True)  # nombre usuario
    email = db.Column(db.String(120), unique=True, nullable=False)  # correo personal
    password = db.Column(db.String(120), nullable=False)  # Encriptar
    productos = db.relationship('Producto', backref='Usuario')


class Producto(db.Model):
    __tablename__ = "Producto"
    codigo_p = db.Column(db.String(6), primary_key=True)
    usuario_p = db.Column(db.String(80), db.ForeignKey('Usuario.username'))
    nombre = db.Column(db.String(40), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    marca = db.Column(db.String(30), nullable=False)
    categoria = db.Column(db.String(30), nullable=False)


class Compra(db.Model):
    __tablename__ = "Compra"
    codigo_c = db.Column(db.String(6), primary_key=True)
    codigo_p = db.Column(db.String(6), db.ForeignKey('Producto.codigo_p'))
    usuario_c = db.Column(db.String(80), db.ForeignKey('Usuario.username'))
    usuario_v = db.Column(db.String(80), db.ForeignKey('Usuario.username'))
    # me gustaria agregar una columna fecha que guarde la fecha en tiempo real
