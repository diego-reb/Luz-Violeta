from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100),nullable = False)
    correo = db.Column (db.String(100), nullable = False, unique = True)
    contrasena = db.Column(db.String(100), nulable = False)
    nombre_usuario = db.Column(db.String(50), nullable = False, unique = True)
    activo = db.Column(db.Boolean, default = True)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id_rol'), nullable = False)

    rol = relationship('Rol', back_populates = 'usuarios')

    def set_password(self, password):
        self.contraseña_hash = generate_password_hash(password)


    def check_password (self, password):
        return check_password_hash(self.contrasela_hash, password)






