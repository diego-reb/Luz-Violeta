from app.extensiones import db

class Albergue(db.Model):
    __tablename__ = 'albergues'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    direccion = db.Column(db.Text)
    telefono = db.Column(db.String(50))
    codigo_postal = db.Column(db.String(10))
    latitud = db.Column(db.Numeric(10, 6))
    longitud = db.Column(db.Numeric(10, 6))
    id_alcaldia = db.Column(db.Integer, db.ForeignKey('alcaldias.id'))

    alcaldia = db.relationship('Alcaldia', back_populates='albergues')

    def __repr__(self):
        return f"<Albergue {self.nombre}>"
