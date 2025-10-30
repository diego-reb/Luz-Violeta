from functools import wraps
from flask import session, redirect, url_for, make_response

def login_required(role_id=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'usuario_id' not in session:
                return redirect(url_for('login_bp.login'))

            if role_id is not None and session.get('rol_id') != role_id:
                return redirect(url_for('login_bp.login'))

            # Ejecuta la vista
            response = make_response(f(*args, **kwargs))
            # Evitar cache del navegador
            response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, private, max-age=0'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
            return response
        return decorated_function
    return decorator
