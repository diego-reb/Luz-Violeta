from app.extensiones import db

class Alcaldia(db.Model):
    __tablename__ = 'alcaldias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    clave_inegi = db.Column(db.String(10))

    # Relación con Albergues
    albergues = db.relationship('Albergue', backref='alcaldia', lazy=True)

    def __repr__(self):
        return f"<Alcaldia {self.nombre}>"
