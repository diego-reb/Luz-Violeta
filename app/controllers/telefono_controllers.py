from flask import Blueprint, jsonify
from app.extensiones import db
from datetime import datetime

telefono_bp = Blueprint('telefono', __name__)

@telefono_bp.route('/registrar_click_telefono', methods=['POST'])
def registrar_click_telefono():
    try:
        db.execute("INSERT INTO clicks_telefono (fecha) VALUES (:fecha)", {"fecha": datetime.now()})
        db.session.commit()
        return jsonify({"status": "ok"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)})
