from flask import Blueprint
admin_bp = Blueprint('admin', __name__, url_prefix = '/administrador')

from app.controllers.admin.adminController import admin_bp
