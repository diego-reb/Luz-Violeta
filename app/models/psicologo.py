from app.extensiones import db

class Psicologo(db.Model):
    __tablename__ = 'psicologos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    telefono_contacto = db.Column(db.String(50))
    correo_contacto = db.Column(db.String(100))
    costo = db.Column(db.String(100))
    direccion = db.Column(db.Text)
    latitud = db.Column(db.Numeric(10, 6))
    longitud = db.Column(db.Numeric(10, 6))

    def __repr__(self):
        return f"<Psicologo {self.nombre}>"
