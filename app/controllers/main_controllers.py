from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/apoyo_psicologico')
def apoyo_psicologico():
    return render_template('psicologico.html')
