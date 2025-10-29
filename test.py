from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text 

app = Flask(__name__)
app.config.from_object("app.config.Config")

db = SQLAlchemy(app)

def probar_conexion():
    try: 
        with app.app_context():
            print("Probando conexion")
            result = db.session.execute(text("SELECT 1"))
            print("Conexion exitosa")
    except Exception as e:
        print("Error de conexion:", e)

if __name__ == "__main__":  
    probar_conexion()