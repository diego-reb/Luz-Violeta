from flask import Blueprint, render_template, request, redirect, session, url_for, flash, jsonify
from werkzeug.security import check_password_hash
from app.models.usuario import Usuario

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        identificador = request.form.get('identificador')
        password = request.form.get('password')

        if not identificador or not password:
            return render_template("login.html", mensaje = "Faltan campos")
        
        usuario = Usuario.query.filter(
            (Usuario.nombre_usuario == identificador) | (Usuario.correo == identificador)
        ).first()



        if not usuario or not usuario.check_password(password):
            return render_template ("login.html", mensaje = "credenciales invalidas")
        
        session["usuario_id"] = usuario.id_usuario
        session["rol_id"] = usuario.rol_id
        session["nombre"] = usuario.nombre_usuario

        if usuario.rol_id == 1:
            return redirect(url_for('admin.dashboard'))
        else: 
            return redirect(url_for('main.index'))
        
    return render_template("login.html")

