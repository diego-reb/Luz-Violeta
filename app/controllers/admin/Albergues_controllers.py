from flask import Blueprint, render_template, request, jsonify, session, jsonify
from app.extensiones import db
from app.models.albergue import Albergue
from app.utils.decorators import login_required

admin_albergues_bp = Blueprint('admin_albergues_bp', __name__, url_prefix='/admin/Gestion_Albergues')

@admin_albergues_bp.route('/')
@login_required(role_id=1)
def GestionAlbergues():

    page = request.args.get('page', 1, type=int)
    per_page = 10

    pagination = Albergue.query.paginate(page=page, per_page=per_page)
    albergues = Albergue.query.all()
    return render_template('adm_albergues.html', albergues=pagination.items, pagination=pagination)

@admin_albergues_bp.route('/albergue/<int:id>', methods=['GET'])
def obtener_albergue(id):
    a = Albergue.query.get(id)
    return {
        "id": a.id,
        "nombre": a.nombre,
        "direccion": a.direccion,
        "telefono": a.telefono,
        "codigo_postal": a.codigo_postal,
        "latitud": str(a.latitud),
        "longitud": str(a.longitud),
        "id_alcaldia": a.id_alcaldia

    }

@admin_albergues_bp.route('/editar/<int:id>', methods=['PUT'])
def editar_albergue(id):
    a = Albergue.query.get(id)
    data = request.json
    a.nombre = data['nombre']
    a.direccion = data['direccion']
    a.telefono = data['telefono']
    a.codigo_postal = data['codigo_postal']
    a.latitud = data['latitud']
    a.longitud = data['longitud']
    a.id_alcaldia = data['id_alcaldia']

    db.session.commit()
    return jsonify({"status": "ok"}), 200
    
@admin_albergues_bp.route('/registrar', methods=['POST'])
def registrar_albergue():
    data = request.json

    nuevo = Albergue(
        nombre=data['nombre'],
        ciudad=data['ciudad'],
        capacidad=data['capacidad'],
        ocupacion=data['ocupacion'],
        estado=data['estado']
    )

    db.session.add(nuevo)
    db.session.commit()

    return jsonify({"status": "ok"}), 201

@admin_albergues_bp.route('/eliminar/<int:id>', methods=['DELETE'])
def cambiar_estado_usuario(id):
    a = Albergue.query.get(id)
    data = request.json
    a.activo = data['activo']
    db.session.commit()
    return jsonify({"status": "ok"}), 200
    

