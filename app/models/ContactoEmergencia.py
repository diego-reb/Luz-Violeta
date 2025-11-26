from app.extensiones import db
from sqlalchemy.dialects.postgresql import ENUM
from datetime import datetime

relacion_tipo = ENUM(
    'familia', 'amigo', 'pareja', 'vecino', 'compañero', 'otro',
    name='relacion_tipo',
    create_type=False  
)

class ContactoEmergencia(db.Model):
    __tablename__ = 'contacto_emergencia'

    id_contacto = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario', ondelete='CASCADE'), nullable=False)
    nombre_completo = db.Column(db.String(150), nullable=False)
    relacion = db.Column(relacion_tipo, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)

    usuario = db.relationship('Usuario', backref=db.backref('contactos_emergencia', cascade='all, delete-orphan'))

    def __repr__(self):
        return f"<ContactoEmergencia {self.nombre_completo} ({self.relacion})>"