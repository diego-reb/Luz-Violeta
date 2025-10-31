from flask import Blueprint, render_template, session
from app.extensiones import db
from app.models.usuario import Usuario
from app.models.Rol import Rol
from app.utils.decorators import login_required

gestion_usuarios_bp = Blueprint('gestion_usuarios_bp', __name__, url_prefix='/admin/Gestion_Usuarios')

@gestion_usuarios_bp.route('/')
@login_required (role_id=1)
def GestionUsuarios():
    roles = Rol.query.all()
    usuarios = Usuario.query.all()
    return render_template('gestiondeusuariosadmin.html', usuarios=usuarios, roles=roles)
