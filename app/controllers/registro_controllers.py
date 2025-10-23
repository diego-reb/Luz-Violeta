from flask import Blueprint, request, jsonify, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from app.models.usuario import Usuario
from app.extensiones import db

registro_bp = Blueprint('registro_bp', __name__)


@registro_bp.route('/registro', methods=['GET'])
def mostrar_formulario():
    return render_template('registro.html')


@registro_bp.route('/registro', methods=['POST'])
def registrar_usuario():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    nombre = request.form.get('name')
    correo = request.form.get('email')
    nombre_usuario = request.form.get('nombre_usuario')
    contrasena = request.form.get('password')
    confirm_contraseña = request.form.get('confirm-password')

    if not all([nombre, correo, nombre_usuario, contrasena, confirm_contraseña]):
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400
    
    if contrasena != confirm_contraseña:
        return jsonify({'error': 'Las contraseñas no coinciden'}), 400
    
    if Usuario.query.filter_by(correo=correo).first():
        return jsonify({'error': 'El correo ya esta registrado'}), 400
    
    if Usuario.query.filter_by(nombre_usuario = nombre_usuario).first():
        return jsonify({'error': 'El nombre de usuario ya esta en uso'}), 400
    
    hash_contraseña = generate_password_hash(contrasena)
    nuevo_usuario = Usuario(
        nombre=nombre,
        correo=correo,
        nombre_usuario=nombre_usuario, 
        rol_id=2
        )
    nuevo_usuario.set_password(contrasena)

    db.session.add(nuevo_usuario)
    db.session.commit()
    
    if request.is_json:
        return ({'mesaje': 'Usuario registrado exitosamente'}),201

    return redirect('/login')