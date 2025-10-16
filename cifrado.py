from app import Luzvioleta
from app.extensiones import db
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash

# Inicializa la app
app = Luzvioleta()

# Crear contexto de aplicación
with app.app_context():
    usuarios = Usuario.query.all()

    for usuario in usuarios:
        if not usuario.contrasena.startswith('pbkdf2:sha256:'):
            usuario.contrasena = generate_password_hash(usuario.contrasena)
            print(f"Contraseña actualizada para: {usuario.nombre_usuario}")

    db.session.commit()
    print("✅ Todas las contraseñas fueron cifradas correctamente.")
