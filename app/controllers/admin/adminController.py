from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import admin_bp

@admin_bp.route('/')
def dashboard():
    return render_template('usuariosadm.html')