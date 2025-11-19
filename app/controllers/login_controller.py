from flask import Blueprint, render_template, request, redirect, session, url_for, flash, jsonify
from werkzeug.security import check_password_hash
from app.models.Usuario import Usuario
login_bp = Blueprint('login_bp', __name__)

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
