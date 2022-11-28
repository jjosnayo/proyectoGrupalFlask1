from flask import request, jsonify
from app import db
from app import models
from app.models import Usuario


def index():
    return "pagina principal"


# Ruta para pasar los datos de registro del cliente a la base de datos
def register():
    nuevo_usuario = request.get_json()
    nombre = nuevo_usuario['nombre']
    telefono = nuevo_usuario['telefono']
    direccion = nuevo_usuario['direccion']
    nombre_usuario = nuevo_usuario['nombre_usuario']
    email = nuevo_usuario['email']
    contrasenha = nuevo_usuario['contrasenha']
    try:
        newUser = models.Usuario(name=nombre, phone=telefono, adress=direccion, username=nombre_usuario,
                                 email=email, password=contrasenha)
        db.session.add(newUser)
        db.session.commit()
        return jsonify({"respuesta": "Usuario registrado"})
    except Exception as err:
        print(err)
        return jsonify({"respuesta": "El usuario ya existe"})


# Ruta para pasar los datos de los usuarios de la base de datos al cliente
def usuarios():
    usuarios_e = Usuario.query.all()
    usuarios_l = []
    for i in usuarios_e:
        usuario_d = {"nombre": i.name, "telefono": i.phone, "direccion": i.adress, "nombre_usuario": i.username,
                     "email": i.email, "contrasenha": i.password}
        usuarios_l.append(usuario_d)
    return jsonify(usuarios_l)


# Ruta para verificar los datos del login del cliente mediante la base de datos
def login():
    usuario_v = request.get_json()
    l_usuario = usuario_v['nombre_usuario']
    l_contrasenha = usuario_v['contrasenha']
    usuario_r = Usuario.query.filter(Usuario.username == l_usuario and Usuario.password == l_contrasenha)
    usuario_rd = {"nombre_usuario": usuario_r.username, "contrasenha": usuario_r.password}
    return jsonify(usuario_rd)


def registrar_producto():
    return "registrar producto"


def vender():
    return "vender"


def comprar():
    return "comprar"


def inventario():
    return "inventario"
