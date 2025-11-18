from flask import Blueprint, render_template, session, redirect, url_for
from app.utils.decorators import login_required
from app.models.Usuario import Usuario
from app.models.abogado import Abogado
from app.models.albergue import Albergue
from app.models.psicologo import Psicologo
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
        solicitudes_albergues = Albergue.query.count()
        consultas_legales = Abogado.query.count()
        voluntarios = Psicologo.query.count()

        tareas = [
            "Revisar 3 nuevas solicitudes de albergues.",
            "Responder mensajes de usuario #1234.",
            "Actualizar la lista de contactos de emergencia."
        ]
       
        return render_template('sesionadmin.html', nombre=nombre, usuarios_activos=usuarios_activos, solicitudes_albergues=solicitudes_albergues, consultas_legales=consultas_legales, voluntarios=voluntarios,tareas=tareas)
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
    
