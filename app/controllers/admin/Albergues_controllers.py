from flask import Blueprint, render_template, request, jsonify
from app.extensiones import db
from app.models.albergue import Albergue
from app.utils.decorators import login_required
from app.models.alcaldia import Alcaldia

admin_albergues_bp = Blueprint('admin_albergues_bp', __name__, url_prefix='/admin/Gestion_Albergues')


@admin_albergues_bp.route('/')
@login_required(role_id=1)
def GestionAlbergues():

    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    alcaldias = Alcaldia.query.all()

    pagination = Albergue.query.paginate(page=page, per_page=per_page)
    
    return render_template(
        'adm_albergues.html',
        albergues=pagination.items,
        pagination=pagination,
        alcaldias=alcaldias
    )


@admin_albergues_bp.route('/albergue/<int:id>', methods=['GET'])
def obtener_albergue(id):
    a = Albergue.query.get(id)
    return {
        "id": a.id,
        "nombre": a.nombre,
        "capacidad_total": a.capacidad_total,
        "capacidad_ocupada": a.capacidad_ocupada,
        "estado": a.estado,
        "alcaldia_id": a.id_alcaldia,
        "alcaldia_nombre": a.alcaldia.nombre if a.alcaldia else None
    }


@admin_albergues_bp.route('/registrar', methods=['POST'])
def registrar_albergue():
    data = request.json

    capacidad_total = int(data['capacidad_total'])
    capacidad_ocupada = int(data['capacidad_ocupada'])
    if capacidad_ocupada > capacidad_total:
        return jsonify({
            "success": False,
            "message": "La capacidad ocupada no puede ser mayor que la capacidad total"
        })
    nuevo = Albergue(
        nombre=data['nombre'],
        id_alcaldia=data['alcaldia_id'],
        direccion=data['direccion'],
        telefono=data['telefono'],
        codigo_postal=data['codigo_postal'],
        latitud=data['latitud'],
        longitud=data['longitud'],
        capacidad_total=data['capacidad_total'],
        capacidad_ocupada=data['capacidad_ocupada'],
        estado=data['estado']
    )

    db.session.add(nuevo)
    db.session.commit()

    
    return jsonify({
        "success": True,
        "message": "Albergue registrado correctamente"
    }), 201


@admin_albergues_bp.route('/editar/<int:id>', methods=['PUT'])
def editar_albergue(id):
    a = Albergue.query.get(id)
    data = request.json

    capacidad_total = int(data['capacidad_total'])
    capacidad_ocupada = int(data['capacidad_ocupada'])
    if capacidad_ocupada > capacidad_total:
        return jsonify({
            "success": False,
            "message": "La capacidad ocupada no puede ser mayor que la capacidad total"
        })

    a.nombre = data['nombre']
    a.id_alcaldia = data['alcaldia_id']
    a.direccion = data['direccion']
    a.telefono = data['telefono']
    a.codigo_postal = data['codigo_postal']
    a.latitud = data['latitud']
    a.longitud = data['longitud']
    a.capacidad_total = data['capacidad_total']
    a.capacidad_ocupada = data['capacidad_ocupada']
    a.estado = data['estado']

    db.session.commit()
    return jsonify({
        "success": True,
        "message": "Albergue actualizado correctamente"
    }), 200


@admin_albergues_bp.route('/eliminar/<int:id>', methods=['DELETE'])
def eliminar_albergue(id):
    a = Albergue.query.get(id)

    if not a:
        return jsonify({"success": False, "message": "Albergue no encontrado"}), 404

    a.estado = "Cerrado"
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Albergue eliminado correctamente"
    }), 200



@admin_albergues_bp.route('/alcaldias', methods=['GET'])
def obtener_alcaldias():
    alcaldias = Alcaldia.query.all()
    return jsonify([
        {"id": a.id, "nombre": a.nombre}
        for a in alcaldias
    ])
