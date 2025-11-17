from app.extensiones import db
from flask import Blueprint, render_template, request
from app.models.psicologo import Psicologo
from app.models.alcaldia import Alcaldia

psicologo_bp = Blueprint('psicologo_bp', __name__, url_prefix='/psicologo')

@psicologo_bp.route ('/')
def psicologo():
    try:
        psicologos = Psicologo.query.all()
        alcaldias = Alcaldia.query.all()
        return render_template('psicologico.html', psicologos=psicologos, alcaldias=alcaldias)
    except Exception as e:
        print(f"Error al cargar página de psicologos")
        return render_template('error_generico.html',mensaje="Error al cargar los abogados") 