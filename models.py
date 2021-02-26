from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)
    apellido = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    phone = db.Column(db.String(200), nullable=False)
    created = db.Column(db.DateTime(), default=db.func.now())
    agendamiento = db.relationship('Agendamiento', backref='users')

    def serialize(self):
         return {
             "id": self.id,
             "username": self.username,
             "apellido": self.apellido,
             "email": self.email,
             "phone": self.phone,
         }
    
    def serialize_with_servicio_extra(self):
         return {
             "id": self.id,
             "username": self.username,
             "apellido": self.apellido,
             "email": self.email,
             "phone": self.phone,
             "agendamiento": self.get_agendamiento(),
         }

    def get_agendamiento(self):
        return list(map(lambda agendamiento: agendamiento.serialize, self.agendamiento))

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
    id = db.Column(db.Integer, primary_key=True, unique=True) #Clave primaria de tabla
    nombre_servicio = db.Column(db.String(200))
    valor_servicio = db.Column(db.String(200))

    def serialize(self):
         return {
             "id": self.id,
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
    id = db.Column(db.Integer, primary_key=True) #Clave primaria de tabla
    fechas = db.Column(db.DateTime, nullable=False)
    horas = db.Column(db.String(200), nullable=False)

    def serialize(self):
         return {
             "id": self.id,
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
    id = db.Column(db.Integer, primary_key=True, unique=True) #Clave primaria de tabla
    valor_extra = db.Column(db.String(200))
    nombre_extra = db.Column(db.String(200))

    def serialize(self):
         return {
             "id": self.id,
             "valor_extra": self.valor_extra,
             "nombre_extra": self.nombre_extra,
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
    id = db.Column(db.Integer, primary_key=True) #Clave primaria de tabla
    servicio = db.Column(db.String(200))
    extra = db.Column(db.String(200))
    fecha = db.Column(db.String(200))
    hora = db.Column(db.String(200))
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "servicio": self.servicio,
            "extra": self.extra,
            "fecha": self.fecha,
            "hora": self.hora,
         }
    def serialize_with_user(self):
        return {
            "id": self.id,
            "servicio": self.servicio,
            "extra": self.extra,
            "fecha": self.fecha,
            "hora": self.hora,
         }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(seld):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()