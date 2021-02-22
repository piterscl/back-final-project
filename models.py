from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    phone = db.Column(db.String(200), nullable=False)
    created = db.Column(db.DateTime(), default=db.func.now())
    agendamientos_users = db.relationship('Agendamiento', backref='users')

    def serialize(self):
         return {
             "id": self.id,
             "username": self.username,
             "email": self.email,
             "phone": self.phone,
         }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(seld):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Servicios(db.Model):
    __tablename__ = 'servicios'
    servicio_id = db.Column(db.Integer, primary_key=True, unique=True) #Clave primaria de tabla
    nombre_servicio = db.Column(db.String(200))
    valor_servicio = db.Column(db.String(200))
    agendamientos_servicios = db.relationship('Agendamiento', uselist=False, backref='servicios')

    def serialize(self):
         return {
             "servicio_id": self.servicio_id,
             "nombre_servicio": self.nombre_servicio,
             "valor_servicio": self.valor_servicio,
         }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(seld):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Horarios(db.Model):
    __tablename__ = 'horarios'
    horarios_id = db.Column(db.Integer, primary_key=True) #Clave primaria de tabla
    fechas = db.Column(db.DateTime)
    horas = db.Column(db.String(200))
    agendamientos_horarios = db.relationship('Agendamiento', uselist=False, backref='horarios')

    def serialize(self):
         return {
             "horarios_id": self.horarios_id,
             "fechas": self.fechas,
             "horas": self.horas ,
         }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(seld):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Extras(db.Model):
    __tablename__ = 'extras'
    extras_id = db.Column(db.Integer, primary_key=True) #Clave primaria de tabla
    valor_extra = db.Column(db.String(200))
    nombre_extra = db.Column(db.String(200))
    agendamientos_extras = db.relationship('Agendamiento', backref='extras')

    def serialize(self):
         return {
             "extras_id": self.extras_id,
             "valor_extra": self.valor_extra,
             "nombre_extra": self.nombre_extra ,
         }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(seld):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit() 

class Agendamiento(db.Model):
    __tablename__ = 'agendamiento'
    agendamiento_id = db.Column(db.Integer, primary_key=True) #Clave primaria de tabla
    f_horarios_id = db.Column(db.Integer, db.ForeignKey('horarios.horarios_id'), nullable=False)
    f_servicios_id = db.Column(db.Integer, db.ForeignKey('servicios.servicio_id'), nullable=False)
    f_extras_id = db.Column(db.Integer, db.ForeignKey('extras.extras_id'), nullable=False)
    f_users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    def serialize(self):
        return {
            "agendamiento_id": self.agendamiento_id,
            "f_horarios_id": self.f_horarios_id,
            "f_servicios_id": self.f_servicios_id,
            "f_extras_id": self.f_extras_id,
            "f_users_id": self.f_users_id, 
         }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(seld):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()