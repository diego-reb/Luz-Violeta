from flask import Blueprint, render_template, session, redirect, url_for
from app.utils.decorators import login_required
from app.models.Usuario import Usuario
from app.models.abogado import Abogado
from app.models.albergue import Albergue
from app.models.psicologo import Psicologo
from app.models.Boton_panico import BotonPanico
from app.extensiones import db

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')

@admin_bp.app_context_processor
def inject_user():
    """
    Hace que {{ nombre }} esté disponible en los templates del admin.
    """
    return dict(nombre=session.get('nombre', 'Administrador'))

@admin_bp.route('/')
@login_required(role_id=1)
def dashboard():
    try:
        if "usuario_id" not in session:
            return redirect(url_for("login_bp.login"))
        nombre = session.get("nombre")
        usuarios_activos = Usuario.query.filter_by(activo=True).count()
        albergues_registrados = Albergue.query.count()
        abogados_registrados = Abogado.query.count()
        botones_panico = BotonPanico.query.count()


        return render_template('sesionadmin.html', nombre=nombre, usuarios_activos=usuarios_activos, albergues_registrados=albergues_registrados, abogados_registrados=abogados_registrados, botones_panico=botones_panico)
    except Exception as e:
        print("Error en dashboard.", e)
        return render_template("error_generico.html", mensaje="Error al cargar el panel del administrador")



@admin_bp.route('/Actualizacion_Inegi')
@login_required (role_id=1)
def ActualizacionInegi():
    return render_template('inegi.html')

@admin_bp.route('/Alberges')
@login_required (role_id=1)
def AlberguesAdmin():
    return render_template('alberge_administrador')
    
