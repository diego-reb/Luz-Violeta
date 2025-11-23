from flask import render_template, Blueprint, session, jsonify, request
from app.extensiones import db
from app.models.Boton_panico import BotonPanico

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/boton_panico', methods=['POST'])
def presionar_boton():
    try:
        usuario_id = session.get("usuario_id")  
        evento = BotonPanico(usuario_id=usuario_id)
        db.session.add(evento)
        db.session.commit()
        return jsonify({"success": True, "mensaje": "Botón presionado registrado"})
    except Exception as e:
        print("Error al registrar botón:", e)
        return jsonify({"success": False, "mensaje": "Error al registrar botón"})
