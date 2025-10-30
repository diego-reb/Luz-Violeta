from app.extensiones import db

class CentroAyuda(db.Model):
    __tablename__='centros_ayuda'

    id_centro = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    tipo = db.Column(db.String(100))
    direccion = db.Column(db.String(200))
    id_alcaldia = db.Column(db.Integer, db.ForeignKey('alcaldias.id_alcaldia'))
    telefono = db.Column(db.String(20))
    correo = db.Column(db.String(100))
    horario = db.Column(db.String(100))
    latitud = db.Column(db.Numeric(10,6))
    longitud = db.Column(db.Numeric(10,6))
    activo = db.Column(db.Boolean, default=True)
    id_inegi = db.Column(db.String(50))
    fecha_actualizacion = db.Column(db.Date)

    alcaldia = db.relationship('Alcaldia', back_populates='centros_ayuda')

    def __rep__(self):
        return f'<CentroAyuda {self.nombre}>'