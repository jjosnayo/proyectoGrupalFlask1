from flask import request, jsonify
from app import db
from app import models
from app.models import Usuario, Producto, Compra


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
    nuevo_producto = request.get_json()
    codigo = nuevo_producto['codigo']
    usuario = nuevo_producto['usuario']
    nombre = nuevo_producto['nombre']
    precio = nuevo_producto['precio']
    marca = nuevo_producto['marca']
    categoria = nuevo_producto['categoria']
    try:
        newProduct = models.Producto(codigo_p=codigo, usuario_p=usuario, nombre=nombre, precio=precio,
                                     marca=marca, categoria=categoria)
        db.session.add(newProduct)
        db.session.commit()
        return jsonify({"respuesta": "Producto registrado"})
    except Exception as err:
        print(err)
        return jsonify({"respuesta": "El producto ya existe"})


def vender():
    producto_u = request.get_json()
    usuario_l = producto_u['usuario']
    productos_l = Producto.query.filter(Producto.usuario_p == usuario_l)
    productos_d = []
    for i in productos_l:
        producto_d = {"codigo": i.codigo_p, "nombre": i.nombre,
                      "precio": i.precio, "marca": i.marca, "tipo": i.categoria}
        productos_d.append(producto_d)
    return jsonify(productos_d)


def comprar():
    producto_u = request.get_json()
    usuario_l = producto_u['usuario']
    productos_nl = Producto.query.filter(Producto.usuario_p != usuario_l)
    productos_d = []
    for i in productos_nl:
        producto_d = {"codigo": i.codigo_p, "usuario_nombre": i.usuario_p, "nombre": i.nombre,
                      "precio": i.precio, "marca": i.marca, "tipo": i.categoria}
        productos_d.append(producto_d)
    return jsonify(productos_d)


def registrar_compra():
    nueva_compra = request.get_json()
    codigo_p = nueva_compra['codigo_producto']
    comprador = nueva_compra['usuario_comprador']
    vendedor = nueva_compra['usuario_vendedor']
    try:
        newPurchase = models.Compra(codigo_p=codigo_p, usuario_c=comprador, usuario_v=vendedor)
        db.session.add(newPurchase)
        db.session.commit()
        return jsonify({"respuesta": "Compra registrada"})
    except Exception as err:
        print(err)
        return jsonify({"respuesta": "La compra ya existe"})


def inventario():
    compra_u = request.get_json()
    usuario_l = compra_u['usuario']
    compras_l = Compra.query.filter(Compra.usuario_c == usuario_l)
    compras_d = []
    for i in compras_l:
        compra_d = {"codigo_c": i.codigo_c, "codigo_p": i.codigo_p,
                    "usuario_c": i.usuario_c, "usuario_v": i.usuario_v}
        compras_d.append(compra_d)
    return jsonify(compras_d)
