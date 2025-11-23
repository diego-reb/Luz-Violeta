from datetime import datetime
from app.extensiones import db
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class BotonPanico(db.Model):
    __tablename__ = 'boton_panico'
    id_boton = db.Column(db.Integer, primary_key = True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable = False)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())

    
    def __repr__(self):
        return f"<BotonPanico {self.id_boton} - {self.fecha}>"