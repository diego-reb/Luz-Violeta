from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def Luzvioleta():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.controllers.main_controllers import main
    app.register_blueprint(main)

    ##from app.controllers.usuario_controller import usuario_bp
    ##from app.controllers.admin_controller import admin_bp

    ##app.registaer_blueprint(usuario_bp, url_prefix="/usuario")
    ##app.register_blueprint(admin_bp, url_prefix="/admin")

    return app