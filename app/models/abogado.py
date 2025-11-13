from app.extensiones import db

class Abogado(db.Model):
    __tablename__ = 'abogados'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(50))
    correo = db.Column(db.String(100))
    costo = db.Column(db.String(100))
    direccion = db.Column(db.Text)
    latitud = db.Column(db.Numeric(10, 6))
    longitud = db.Column(db.Numeric(10, 6))

    def __repr__(self):
        return f"<Abogado {self.nombre}>"
