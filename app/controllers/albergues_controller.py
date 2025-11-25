from flask import Blueprint, render_template, jsonify, current_app
from app.models.alcaldia import Alcaldia
from app.models.albergue import Albergue
from app.extensiones import db

albergues_bp = Blueprint('albergues_bp', __name__, url_prefix='/albergues')

@albergues_bp.route('/')
def albergues():
    try:
        alcaldias = Alcaldia.query.all()
        albergues = Albergue.query.all()
        api_key = current_app.config.get("MAPS_API_KEY")
        return render_template('albergues.html', alcaldias=alcaldias, albergues=albergues, maps_api_key=api_key)
    except Exception as e:
        print(f"Error al cargar página de albergues: {e}")
        return render_template('error_generico.html', mensaje="Error al cargar los albergues")

@albergues_bp.route('/por_alcaldia/<int:id_alcaldia>')
def albergues_por_alcaldia(id_alcaldia):
    try:
        albergues = Albergue.query.filter_by(id_alcaldia=id_alcaldia).all()
        
        data = [
            {
                "id": a.id,
                "nombre": a.nombre,
                "direccion": a.direccion or "Sin dirección registrada",
                "telefono": a.telefono or "No disponible",
                "latitud": float(a.latitud) if a.latitud else None,
                "longitud": float(a.longitud) if a.longitud else None,
            }
            for a in albergues
        ]

        return jsonify(data)
    except Exception as e:
        print(f"Error al obtener albergues de la alcaldía {id_alcaldia}: {e}")
        return jsonify({"error": "Error al cargar los albergues"}), 500
