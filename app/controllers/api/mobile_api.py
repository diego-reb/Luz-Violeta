import hmac
import hashlib
import os
from flask import Blueprint, jsonify, current_app, request
from app.models.albergue import Albergue
from app.models.alcaldia import Alcaldia
from app.models.abogado import Abogado
from app.models.psicologo import Psicologo
from app.models.Usuario import Usuario
from app.models.ContactoEmergencia import ContactoEmergencia
from app.extensiones import db

mobile_api_bp = Blueprint('mobile_api_bp', __name__, url_prefix='/api')

# ─── AUTH ─────────────────────────────────────────────────────────────────────

def _make_token(user_id: int) -> str:
    """Token simple: HMAC-SHA256(user_id, SECRET_KEY)"""
    secret = os.environ.get('SECRET_KEY', 'dev-secret').encode()
    msg = str(user_id).encode()
    sig = hmac.new(secret, msg, hashlib.sha256).hexdigest()
    return f"{user_id}.{sig}"

def _verify_token(token: str):
    """Devuelve user_id si el token es válido, None si no."""
    try:
        user_id_str, sig = token.rsplit('.', 1)
        expected = _make_token(int(user_id_str))
        if hmac.compare_digest(expected, token):
            return int(user_id_str)
    except Exception:
        pass
    return None

def _get_current_user():
    """Extrae el usuario del header Authorization: Bearer <token>"""
    auth = request.headers.get('Authorization', '')
    if not auth.startswith('Bearer '):
        return None
    token = auth[7:]
    user_id = _verify_token(token)
    if not user_id:
        return None
    return Usuario.query.get(user_id)

def _require_auth():
    """Retorna (usuario, None) o (None, error_response)."""
    usuario = _get_current_user()
    if not usuario:
        return None, (jsonify({'success': False, 'message': 'No autenticado'}), 401)
    return usuario, None

# ─── LOGIN ────────────────────────────────────────────────────────────────────

@mobile_api_bp.route('/login', methods=['POST'])
def api_login():
    """POST /api/login — autenticación móvil con respuesta de token."""
    try:
        data = request.get_json(silent=True) or {}
        identificador = (data.get('identificador') or '').strip()
        password = data.get('password') or ''

        if not identificador or not password:
            return jsonify({'success': False, 'message': 'Completa todos los campos'}), 400

        usuario = Usuario.query.filter(
            (Usuario.nombre_usuario == identificador) | (Usuario.correo == identificador)
        ).first()

        if not usuario or not getattr(usuario, 'activo', True) or not usuario.check_password(password):
            return jsonify({'success': False, 'message': 'Credenciales inválidas'}), 401

        if usuario.rol_id == 1:
            return jsonify({'success': False, 'message': 'Este acceso es solo para usuarias'}), 403

        token = _make_token(usuario.id_usuario)

        return jsonify({
            'success': True,
            'message': 'Inicio de sesión exitoso',
            'token': token,
            'user': {
                'id': usuario.id_usuario,
                'nombre': usuario.nombre,
                'username': usuario.nombre_usuario,
                'email': usuario.correo,
                'rol_id': usuario.rol_id,
                'foto_perfil': usuario.foto_perfil,
                'telefono': usuario.telefono,
                'direccion': usuario.direccion,
                'tipo_sangre': usuario.tipo_sangre,
            },
        }), 200

    except Exception:
        current_app.logger.exception('Error en POST /api/login')
        return jsonify({'success': False, 'message': 'Error inesperado'}), 500

# ─── REGISTRO ─────────────────────────────────────────────────────────────────

@mobile_api_bp.route('/registro', methods=['POST'])
def api_registro():
    """POST /api/registro — crear nueva usuaria."""
    try:
        data = request.get_json(silent=True) or {}
        nombre = (data.get('nombre') or '').strip()
        correo = (data.get('correo') or '').strip().lower()
        nombre_usuario = (data.get('nombre_usuario') or '').strip()
        password = data.get('password') or ''
        confirm_password = data.get('confirm_password') or ''

        if not all([nombre, correo, nombre_usuario, password, confirm_password]):
            return jsonify({'success': False, 'message': 'Todos los campos son obligatorios'}), 400

        if password != confirm_password:
            return jsonify({'success': False, 'message': 'Las contraseñas no coinciden'}), 400

        if len(password) < 6:
            return jsonify({'success': False, 'message': 'La contraseña debe tener al menos 6 caracteres'}), 400

        if Usuario.query.filter_by(correo=correo).first():
            return jsonify({'success': False, 'message': 'El correo ya está registrado'}), 400

        if Usuario.query.filter_by(nombre_usuario=nombre_usuario).first():
            return jsonify({'success': False, 'message': 'El nombre de usuario ya está en uso'}), 400

        nuevo = Usuario(nombre=nombre, correo=correo, nombre_usuario=nombre_usuario, rol_id=2)
        nuevo.set_password(password)
        db.session.add(nuevo)
        db.session.commit()

        token = _make_token(nuevo.id_usuario)
        return jsonify({
            'success': True,
            'message': 'Cuenta creada exitosamente',
            'token': token,
            'user': {
                'id': nuevo.id_usuario,
                'nombre': nuevo.nombre,
                'username': nuevo.nombre_usuario,
                'email': nuevo.correo,
                'rol_id': nuevo.rol_id,
                'foto_perfil': None,
                'telefono': None,
                'direccion': None,
                'tipo_sangre': None,
            },
        }), 201

    except Exception:
        db.session.rollback()
        current_app.logger.exception('Error en POST /api/registro')
        return jsonify({'success': False, 'message': 'Error al crear la cuenta'}), 500

# ─── ALBERGUES ────────────────────────────────────────────────────────────────

@mobile_api_bp.route('/albergues', methods=['GET'])
def api_albergues():
    """GET /api/albergues — todos los albergues con alcaldía."""
    try:
        albergues = Albergue.query.all()
        data = [
            {
                'id': a.id,
                'nombre': a.nombre,
                'direccion': a.direccion or 'Sin dirección registrada',
                'telefono': a.telefono or 'No disponible',
                'latitud': float(a.latitud) if a.latitud else None,
                'longitud': float(a.longitud) if a.longitud else None,
                'capacidad_total': a.capacidad_total,
                'capacidad_ocupada': a.capacidad_ocupada,
                'estado': a.estado or 'Activo',
                'alcaldia': a.alcaldia.nombre if a.alcaldia else 'Sin alcaldía',
            }
            for a in albergues
        ]
        return jsonify({'success': True, 'albergues': data}), 200
    except Exception:
        current_app.logger.exception('Error en GET /api/albergues')
        return jsonify({'success': False, 'message': 'Error al cargar albergues'}), 500

# ─── ALCALDÍAS ────────────────────────────────────────────────────────────────

@mobile_api_bp.route('/alcaldias', methods=['GET'])
def api_alcaldias():
    """GET /api/alcaldias — lista de alcaldías."""
    try:
        alcaldias = Alcaldia.query.order_by(Alcaldia.nombre).all()
        data = [{'id': a.id, 'nombre': a.nombre} for a in alcaldias]
        return jsonify({'success': True, 'alcaldias': data}), 200
    except Exception:
        current_app.logger.exception('Error en GET /api/alcaldias')
        return jsonify({'success': False, 'message': 'Error al cargar alcaldías'}), 500

# ─── ABOGADOS ─────────────────────────────────────────────────────────────────

@mobile_api_bp.route('/abogados', methods=['GET'])
def api_abogados():
    """GET /api/abogados — lista de abogados."""
    try:
        abogados = Abogado.query.all()
        data = [
            {
                'id': a.id,
                'nombre': a.nombre,
                'telefono': a.telefono or 'No disponible',
                'correo': a.correo or 'No disponible',
                'costo': a.costo or 'Consultar',
                'direccion': a.direccion or 'Sin dirección',
                'latitud': float(a.latitud) if a.latitud else None,
                'longitud': float(a.longitud) if a.longitud else None,
            }
            for a in abogados
        ]
        return jsonify({'success': True, 'abogados': data}), 200
    except Exception:
        current_app.logger.exception('Error en GET /api/abogados')
        return jsonify({'success': False, 'message': 'Error al cargar abogados'}), 500

# ─── PSICÓLOGOS ───────────────────────────────────────────────────────────────

@mobile_api_bp.route('/psicologos', methods=['GET'])
def api_psicologos():
    """GET /api/psicologos — lista de psicólogos."""
    try:
        psicologos = Psicologo.query.all()
        data = [
            {
                'id': p.id,
                'nombre': p.nombre,
                'telefono': p.telefono_contacto or 'No disponible',
                'correo': p.correo_contacto or 'No disponible',
                'costo': p.costo or 'Consultar',
                'direccion': p.direccion or 'Sin dirección',
                'latitud': float(p.latitud) if p.latitud else None,
                'longitud': float(p.longitud) if p.longitud else None,
            }
            for p in psicologos
        ]
        return jsonify({'success': True, 'psicologos': data}), 200
    except Exception:
        current_app.logger.exception('Error en GET /api/psicologos')
        return jsonify({'success': False, 'message': 'Error al cargar psicólogos'}), 500

# ─── PERFIL ───────────────────────────────────────────────────────────────────

@mobile_api_bp.route('/perfil', methods=['GET'])
def api_get_perfil():
    """GET /api/perfil — datos del usuario autenticado."""
    usuario, err = _require_auth()
    if err:
        return err
    return jsonify({
        'success': True,
        'user': {
            'id': usuario.id_usuario,
            'nombre': usuario.nombre,
            'username': usuario.nombre_usuario,
            'email': usuario.correo,
            'telefono': usuario.telefono,
            'direccion': usuario.direccion,
            'tipo_sangre': usuario.tipo_sangre,
            'foto_perfil': usuario.foto_perfil,
            'rol_id': usuario.rol_id,
        },
    }), 200

@mobile_api_bp.route('/perfil', methods=['PUT'])
def api_update_perfil():
    """PUT /api/perfil — actualizar datos del perfil."""
    usuario, err = _require_auth()
    if err:
        return err
    try:
        data = request.get_json(silent=True) or {}
        if 'nombre' in data:
            usuario.nombre = data['nombre'].strip()
        if 'nombre_usuario' in data:
            nu = data['nombre_usuario'].strip()
            existing = Usuario.query.filter_by(nombre_usuario=nu).first()
            if existing and existing.id_usuario != usuario.id_usuario:
                return jsonify({'success': False, 'message': 'El nombre de usuario ya está en uso'}), 400
            usuario.nombre_usuario = nu
        if 'correo' in data:
            correo = data['correo'].strip().lower()
            existing = Usuario.query.filter_by(correo=correo).first()
            if existing and existing.id_usuario != usuario.id_usuario:
                return jsonify({'success': False, 'message': 'El correo ya está en uso'}), 400
            usuario.correo = correo
        if 'telefono' in data:
            usuario.telefono = data['telefono'].strip() or None
        if 'direccion' in data:
            usuario.direccion = data['direccion'].strip() or None
        if 'tipo_sangre' in data:
            usuario.tipo_sangre = data['tipo_sangre'].strip() or None

        db.session.commit()
        return jsonify({'success': True, 'message': 'Perfil actualizado correctamente'}), 200
    except Exception:
        db.session.rollback()
        current_app.logger.exception('Error en PUT /api/perfil')
        return jsonify({'success': False, 'message': 'Error al actualizar perfil'}), 500

@mobile_api_bp.route('/cambiar-password', methods=['PUT'])
def api_cambiar_password():
    """PUT /api/cambiar-password — cambiar contraseña."""
    usuario, err = _require_auth()
    if err:
        return err
    try:
        data = request.get_json(silent=True) or {}
        password_actual = data.get('password_actual') or ''
        nueva_password = data.get('nueva_password') or ''
        confirmar = data.get('confirmar_password') or ''

        if not usuario.check_password(password_actual):
            return jsonify({'success': False, 'message': 'La contraseña actual es incorrecta'}), 400

        if nueva_password != confirmar:
            return jsonify({'success': False, 'message': 'Las contraseñas no coinciden'}), 400

        if len(nueva_password) < 6:
            return jsonify({'success': False, 'message': 'La contraseña debe tener al menos 6 caracteres'}), 400

        usuario.set_password(nueva_password)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Contraseña actualizada correctamente'}), 200
    except Exception:
        db.session.rollback()
        current_app.logger.exception('Error en PUT /api/cambiar-password')
        return jsonify({'success': False, 'message': 'Error al cambiar contraseña'}), 500

# ─── CONTACTOS DE EMERGENCIA ──────────────────────────────────────────────────

@mobile_api_bp.route('/contactos', methods=['GET'])
def api_get_contactos():
    """GET /api/contactos — contactos de emergencia del usuario."""
    usuario, err = _require_auth()
    if err:
        return err
    contactos = ContactoEmergencia.query.filter_by(usuario_id=usuario.id_usuario).all()
    data = [
        {
            'id': c.id_contacto,
            'nombre': c.nombre_completo,
            'relacion': c.relacion,
            'telefono': c.telefono,
        }
        for c in contactos
    ]
    return jsonify({'success': True, 'contactos': data}), 200

@mobile_api_bp.route('/contactos', methods=['POST'])
def api_add_contacto():
    """POST /api/contactos — agregar contacto de emergencia."""
    usuario, err = _require_auth()
    if err:
        return err
    try:
        data = request.get_json(silent=True) or {}
        nombre = (data.get('nombre') or '').strip()
        relacion = (data.get('relacion') or '').strip()
        telefono = (data.get('telefono') or '').strip()

        if not all([nombre, relacion, telefono]):
            return jsonify({'success': False, 'message': 'Todos los campos son obligatorios'}), 400

        contacto = ContactoEmergencia(
            usuario_id=usuario.id_usuario,
            nombre_completo=nombre,
            relacion=relacion,
            telefono=telefono,
        )
        db.session.add(contacto)
        db.session.commit()
        return jsonify({
            'success': True,
            'message': 'Contacto agregado',
            'contacto': {
                'id': contacto.id_contacto,
                'nombre': contacto.nombre_completo,
                'relacion': contacto.relacion,
                'telefono': contacto.telefono,
            },
        }), 201
    except Exception:
        db.session.rollback()
        current_app.logger.exception('Error en POST /api/contactos')
        return jsonify({'success': False, 'message': 'Error al agregar contacto'}), 500

@mobile_api_bp.route('/contactos/<int:id_contacto>', methods=['DELETE'])
def api_delete_contacto(id_contacto):
    """DELETE /api/contactos/<id> — eliminar contacto."""
    usuario, err = _require_auth()
    if err:
        return err
    try:
        contacto = ContactoEmergencia.query.filter_by(
            id_contacto=id_contacto,
            usuario_id=usuario.id_usuario,
        ).first()
        if not contacto:
            return jsonify({'success': False, 'message': 'Contacto no encontrado'}), 404
        db.session.delete(contacto)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Contacto eliminado'}), 200
    except Exception:
        db.session.rollback()
        current_app.logger.exception('Error en DELETE /api/contactos')
        return jsonify({'success': False, 'message': 'Error al eliminar contacto'}), 500

# ─── CHAT (IA Gemini) ─────────────────────────────────────────────────────────

@mobile_api_bp.route('/chat', methods=['POST'])
def api_chat():
    """POST /api/chat — chat con IA Gemini."""
    import requests as req_lib
    try:
        data = request.get_json(silent=True) or {}
        user_message = data.get('message', '')
        chat_history = data.get('history', [])

        MODEL_NAME = 'gemini-2.5-flash'
        api_key = os.environ.get('GEMINI_API_KEY', '')
        API_URL = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={api_key}'

        payload = {
            'contents': chat_history + [{'role': 'user', 'parts': [{'text': user_message}]}],
            'generationConfig': {'temperature': 0.7},
        }

        response = req_lib.post(API_URL, json=payload, timeout=20)
        response.raise_for_status()
        result = response.json()
        bot_reply = (
            result.get('candidates', [{}])[0]
            .get('content', {})
            .get('parts', [{}])[0]
            .get('text', 'Sin respuesta')
        )
        return jsonify({'success': True, 'reply': bot_reply}), 200
    except Exception:
        current_app.logger.exception('Error en POST /api/chat')
        return jsonify({'success': False, 'reply': 'Error al conectar con el asistente'}), 500
