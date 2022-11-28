from app import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref


class Usuario(db.Model):
    __tablename__ = "Usuarios"
    name = db.Column(db.String(80), nullable=False)  # nombre real
    phone = db.Column(db.String(9), nullable=False)  # 9 digitos
    adress = db.Column(db.String(120), nullable=False)  # direccion tienda fisica
    # info para el register
    username = db.Column(db.String(80), primary_key=True)  # nombre usuario
    email = db.Column(db.String(120), unique=True, nullable=False)  # correo personal
    password = db.Column(db.String(120), nullable=False)  # Encriptar

    def __repr__(self):
        return '<Usuario {}>'.format(self.username)
