from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from app.extensiones import db
from app.models.Usuario import Usuario
from app.models.ContactoEmergencia import ContactoEmergencia
import cloudinary.uploader


perfil_bp = Blueprint('perfil', __name__, url_prefix='/perfil')

@perfil_bp.route('/')
def ver_perfil():

    user_id = session.get("usuario_id")
    if not user_id:
        return "No autenticado", 401

    usuario=Usuario.query.get(user_id)

    return render_template('perfil.html', usuario=usuario)

@perfil_bp.route('/actualizar', methods=['POST'])
def actualizar_perfil():
    usuario_id = session.get("usuario_id")
    if not usuario_id:
        return jsonify({"error": "No autenticado"}), 401
    
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    # Datos del formulario
    usuario.nombre = request.form.get('nombre')
    usuario.nombre_usuario = request.form.get('nombre_usuario')
    usuario.correo = request.form.get('correo')
    usuario.telefono = request.form.get('telefono')
    usuario.direccion = request.form.get('direccion')
    usuario.tipo_sangre = request.form.get('tipo_sangre')

    archivo = request.files.get('foto')
    if archivo and archivo.filename != "":
        try:
            upload_result = cloudinary.uploader.upload(
                archivo,
                folder="usuarios",
                public_id=f"user_{usuario_id}",
                overwrite=True
            )
            print("Upload Cloudinary:", upload_result)
            usuario.foto_perfil = upload_result["secure_url"]
        except Exception as e:
            print("Error Cloudinary:", e)


    db.session.commit()

    return jsonify({
        "msg": "Perfil actualizado correctamente",
        "foto_url": usuario.foto_perfil
    })

@perfil_bp.route('/guardar_contacto', methods=['POST'])
def guardar_contacto():
    usuario_id = session.get("usuario_id")
    if not usuario_id:
        return jsonify({"error": "No autenticado"}), 401

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Datos no recibidos"}), 400

        nombre = data.get('name')
        relacion = data.get('relationship')
        telefono = data.get('phone')

        if not nombre or not relacion or not telefono:
            return jsonify({"error": "Todos los campos son obligatorios"}), 400

        contacto = ContactoEmergencia(
            usuario_id=usuario_id,
            nombre_completo=nombre,
            relacion=relacion,
            telefono=telefono
        )

        db.session.add(contacto)
        db.session.commit()

        return jsonify({"success": "Contacto agregado correctamente"}), 200

    except Exception as e:
        db.session.rollback()
        print("Error al guardar contacto:", e)
        return jsonify({"error": str(e)}), 500
