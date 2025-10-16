from flask import Blueprint, render_template, redirect, url_for, request, flash

admin_bp = Blueprint('admin', __name__, url_prefix = '/admin')

@admin_bp.route('/')
def dashboard():
    return render_template('usuariosadm.html')