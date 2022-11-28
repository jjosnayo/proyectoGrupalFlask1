from flask import Blueprint
from app.controllers.LoginController import index, register, usuarios, login, vender, \
    registrar_producto, comprar, inventario

login_bp = Blueprint('login_bp', __name__)

login_bp.route("/", methods=["GET"])(index)
login_bp.route("/utecshop/register", methods=["GET", "POST"])(register)
login_bp.route("/utecshop/usuarios", methods=["GET"])(usuarios)
login_bp.route("/utecshop/login", methods=["GET", "POST"])(login)
login_bp.route("/utecshop/vender", methods=["GET", "POST"])(vender)
login_bp.route("/utecshop/registrar_producto", methods=["GET", "POST"])(registrar_producto)
login_bp.route("/utecshop/comprar", methods=["GET", "POST"])(comprar)
login_bp.route("/utecshop/inventario", methods=["GET"])(inventario)
