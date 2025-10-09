from flask import Blueprint, render_templates, request, redirect, session, url_for, flash, jsonify
from werkzeug.security import check_password_hash
from app.models.Usuario import usuarios

login = Blueprint('login', __name__)

@login.route('/login', methods = ['GET', 'POST'])
def login():
    if request.methods == 'POST':
        identificador = request.form.get['identificador']
        password = request.form.get['password']

        if not identificador or not password:
            return render_templates("login.html", mensaje = "Faltan campos")
        
        usuario = usuarios.query.filter(
            (usuarios.nombre_usuario == identificador) | (usuarios.correo == identificador)
        ).first()


        if not usuario or not usuario.check_password(password):
            return render_templates ("login.html", mensaje = "credenciales invalidas")
        
        session[""]

