from flask import Flask
from .config import Config
from app.extensiones import db, migrate
from app.controllers.main_controllers import main
from app.controllers.login_controller import login_bp
from app.controllers.admin.adminController import admin_bp
from app.controllers.admin import admin_bp
from app.controllers.registro_controllers import registro_bp
from app.controllers.telefono_controllers import telefono_bp

def Luzvioleta():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Importar modelos después de inicializar db
    from app.models import Usuario, Rol

    # Registrar blueprints
    app.register_blueprint(main)
    app.register_blueprint(login_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(registro_bp)
    app.register_blueprint(telefono_bp)

    return app
