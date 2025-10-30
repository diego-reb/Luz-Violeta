from flask import Blueprint, render_template, session
from app.utils.decorators import login_required


admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')

@admin_bp.app_context_processor
def inject_user():
    """
    Hace que {{ nombre }} esté disponible en los templates del admin.
    """
    return dict(nombre=session.get('nombre', 'Administrador'))

@admin_bp.route('/')
@login_required (role_id=1)
def dashboard():
    return render_template('sesionadmin.html')
