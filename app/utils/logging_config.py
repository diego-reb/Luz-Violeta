import logging
import os

def configurar_logging(app):
    """Configura el registro de errores para la aplicación Flask."""

    logs_dir = os.path.join(app.root_path, 'logs')
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    log_path = os.path.join(logs_dir, 'errores.log')
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] en %(pathname)s:%(lineno)d → %(message)s'
    )
    file_handler.setFormatter(formatter)

    if not app.logger.handlers:  
        app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.ERROR)
   
    app.logger.info("📄 Sistema de logging configurado correctamente.")
