from app import db

class Rol(db.Model):
    __tablename__ = 'roles'
    id_rol = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False, unique = True)

    usuarios = db.relationship('Usuario',back_populates = 'rol')