from flask import Blueprint, render_template, request, redirect, session, url_for, flash, jsonify
from werkzeug.security import check_password_hash
from app.models.Usuario import Usuario
login_bp = Blueprint('login_bp', __name__)

def _authenticate_user(identificador, password):
    if not identificador or not password:
        return None

    usuario = Usuario.query.filter(
        (Usuario.nombre_usuario == identificador) | (Usuario.correo == identificador)
    ).first()

    if not usuario or not getattr(usuario, "activo", True):
        return None

    # Usa el método del modelo; si no lo tienes, usa check_password_hash
    if hasattr(usuario, "check_password"):
        if not usuario.check_password(password):
            return None
    else:
        if not check_password_hash(usuario.password_hash, password):
            return None

    return usuario

@login_bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        identificador = request.form.get('identificador')
        password = request.form.get('password')

        if not identificador or not password:
            flash("Por favor complete todos los campos", "error")
            return render_template("login.html")
        
        usuario = Usuario.query.filter(
            (Usuario.nombre_usuario == identificador) | (Usuario.correo == identificador)
        ).first()

        if not usuario.activo:
            flash ("Credenciales invalidas", "error")
            return render_template ("login.html")

        if not usuario or not usuario.check_password(password):
            flash ("Credenciales invalidas", "error")
            return render_template ("login.html")
        
        session.clear()
        session["usuario_id"] = usuario.id_usuario
        session["rol_id"] = usuario.rol_id
        session["nombre"] = usuario.nombre_usuario

        if usuario.rol_id == 1:
            return redirect(url_for('admin_bp.dashboard'))
        else: 
            return redirect(url_for('main.index'))
        
    return render_template("login.html")

@login_bp.route('/logout')
def logout():
    session.clear()
    response = redirect(url_for('main.index'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@login_bp.route('/check_session')
def check_session():
    return jsonify(logged_in = 'usuario_id' in session)

@login_bp.route('/api/login', methods=['POST'])
def api_login():
    try:
        data = request.get_json(silent=True) or {}
        identificador = (data.get('identificador') or '').strip()
        password = data.get('password') or ''

        if not identificador or not password:
            return jsonify({
                'success': False,
                'message': 'No fue posible procesar la solicitud',
            }), 400

        usuario = _authenticate_user(identificador, password)

        if not usuario:
            return jsonify({
                'success': False,
                'message': 'No fue posible iniciar sesion',
            }), 401

        # Si quieres bloquear admins en la app, deja este bloque; si no, elimínalo
        if usuario.rol_id == 1:
            return jsonify({
                'success': False,
                'message': 'Este acceso solo está disponible para usuarias',
            }), 403

        return jsonify({
            'success': True,
            'message': 'Inicio de sesion exitoso',
            'user': {
                'id': usuario.id_usuario,
                'nombre': getattr(usuario, 'nombre', None) or usuario.nombre_usuario,
                'username': usuario.nombre_usuario,
                'email': usuario.correo,
                'rol_id': usuario.rol_id,
                'foto_perfil': getattr(usuario, 'foto_perfil', None),
            },
        }), 200

    except Exception:
        # Si tienes current_app importado en este archivo, puedes loguear
        # current_app.logger.exception('Error inesperado en /api/login')
        return jsonify({
            'success': False,
            'message': 'Ocurrio un error inesperado',
        }), 500