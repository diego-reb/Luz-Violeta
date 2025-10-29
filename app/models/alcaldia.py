from app.extensiones import db

class Alcaldia(db.Model):
    __tablename__ = 'alcaldias'

    id_alcaldia = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    centros_ayuda = db.relationship('CentroAyuda', back_populates='alcaldia')