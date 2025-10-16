from flask import Flask
from .config import Config
from app.extensiones import db, migrate
from app.controllers.main_controllers import main
from app.controllers.login_controller import login_bp

def Luzvioleta():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints
    app.register_blueprint(main)
    app.register_blueprint(login_bp)

    return app
