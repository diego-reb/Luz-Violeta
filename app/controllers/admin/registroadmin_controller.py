from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash
from app.extensiones import db
from app.models.Usuario import Usuario

registroadmin_bp = Blueprint('registroadmin_bp', __name__)

@registroadmin_bp.route('/registro_administrador', methods=['GET'])
def mostrar_formularioA():
    return render_template('registro_administrador.html')
@registroadmin_bp.route('/registro_administrador', methods=['POST'])
def registrar_administradores():
    try:
        # Leer datos JSON
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No se recibieron datos'}), 400

        nombre = data.get('nombre_completo')
        correo = data.get('correo')
        nombre_usuario = data.get('nombre_usuario')
        contrasena = data.get('password')
        confirm_contrasena = data.get('confirmar_password')

        if not all([nombre, correo, nombre_usuario, contrasena, confirm_contrasena]):
            return jsonify({'error': 'Todos los campos son obligatorios'}), 400

        if contrasena != confirm_contrasena:
            return jsonify({'error': 'Las contraseñas no coinciden'}), 400

        if Usuario.query.filter_by(correo=correo).first():
            return jsonify({'error':'El correo ya está registrado'}), 400

        if Usuario.query.filter_by(nombre_usuario=nombre_usuario).first():
            return jsonify({'error':'El nombre de usuario ya está registrado'}), 400

        hash_contrasena = generate_password_hash(contrasena)
        nuevo_administrador = Usuario(
            nombre=nombre,
            correo=correo,
            nombre_usuario=nombre_usuario,
            contrasena=hash_contrasena,
            rol_id=1
        )

        db.session.add(nuevo_administrador)
        db.session.commit()

        return jsonify({'mensaje': 'Usuario registrado exitosamente', 'redirect':url_for('login_bp.login')}), 200

    except Exception as e:
        print(f"Error al registrar el usuario: {e}")
        return jsonify({'error': 'Ocurrió un error al registrar el usuario'}), 500
