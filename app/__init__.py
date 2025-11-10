from flask import Flask, render_template
from .config import Config
from app.extensiones import db, migrate
import traceback
from app.controllers.main_controllers import main
from app.controllers.login_controller import login_bp
from app.controllers.admin.adminController import admin_bp
from app.controllers.admin import admin_bp
from app.controllers.registro_controllers import registro_bp
from app.controllers.telefono_controllers import telefono_bp
from app.controllers.admin.usuarios_controllers import gestion_usuarios_bp
from app.utils.logging_config import configurar_logging


def Luzvioleta():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.models import Usuario, Rol

    app.register_blueprint(main)
    app.register_blueprint(login_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(registro_bp)
    app.register_blueprint(telefono_bp)
    app.register_blueprint(gestion_usuarios_bp)

    configurar_logging(app)

    @app.errorhandler(Exception)
    def handle_exception(e):
        code = getattr(e, "code", 500)
        error_trace = traceback.format_exc()

        app.logger.error(f"Error {code}: {e}\n{error_trace}")
        try:
            return render_template(f"{code}.html"), code
        except:
            return render_template("error_generico.html", code=code), code


    return app
