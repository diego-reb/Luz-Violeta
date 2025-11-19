from flask import Blueprint, render_template, session, request, jsonify
from app.extensiones import db
from app.models.Usuario import Usuario
from app.models.Rol import Rol
from app.utils.decorators import login_required

gestion_usuarios_bp = Blueprint('gestion_usuarios_bp', __name__, url_prefix='/admin/Gestion_Usuarios')

@gestion_usuarios_bp.route('/')
@login_required(role_id=1)
def GestionUsuarios():
    roles = Rol.query.all()
    usuarios = Usuario.query.all()
    return render_template('gestiondeusuariosadmin.html', usuarios=usuarios, roles=roles)

@gestion_usuarios_bp.route('/registrar', methods=['POST'])
def registrar_usuario():
    data = request.json
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        correo=data['correo'],
        nombre_usuario=data['username'],
        rol_id=data['rol_id']
    )
    nuevo_usuario.set_password(data['password'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"status": "ok"}), 200

@gestion_usuarios_bp.route('/usuario/<int:id>', methods=['GET'])
def obtener_usuario(id):
    u = Usuario.query.get(id)
    return jsonify({
        "id_usuario": u.id_usuario,
        "nombre": u.nombre,
        "correo":u.correo,
        "username": u.nombre_usuario,
        "rol_id": u.rol_id,
        "activo": u.activo
    })

@gestion_usuarios_bp.route('/editar/<int:id>', methods=['PUT'])
def editar_usuario(id):
    u= Usuario.query.get(id)
    data = request.json
    u.nombre = data['nombre']
    u.correo = data['correo']
    u.nombre_usuario = data['username']
    u.rol_id = data['rol_id']
    u.activo = data['activo']

    if data['password']:
        u.set_password(data['password'])

    db.session.commit()
    return jsonify({"status":"ok"}), 200

@gestion_usuarios_bp.route('/cambiar_estado/<int:id>', methods=['PUT'])
def cambiar_estado_usuario(id):
    u = Usuario.query.get(id)
    data = request.json
    u.activo = data['activo']
    db.session.commit()
    return jsonify({"status":"ok"}),200