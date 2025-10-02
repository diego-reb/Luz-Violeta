from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/Quienes_somos')
def quienes_somos():
    return render_template('inicio.html')

@main.route('/albergues')
def albergues():
    return render_template('albergues.html')

@main.route('/apoyo_legal')
def apoyo_legal():
    return render_template('legal.html')

@main.route('/apoyo_psicologico')
def apoyo_psicologico():
    return render_template('psicologico.html')
