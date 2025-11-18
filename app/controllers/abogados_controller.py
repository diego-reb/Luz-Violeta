from flask import Blueprint, render_template
from app.extensiones import db
from app.models.abogado import Abogado
from app.models.alcaldia import Alcaldia

abogados_bp = Blueprint('abogados_bp', __name__, url_prefix='/apoyo_legal')

@abogados_bp.route('/')
def abogados():
    try:
        abogados = Abogado.query.all()
        alcaldias = Alcaldia.query.all()
        return render_template('legal.html', alcaldias=alcaldias, abogados=abogados)
    except Exception as e:
        print(f"Error al cargar página de abogados")
        return render_template('error_generico.html', mensaje="Error al cargar los abogados")
