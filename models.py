from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    phone = db.Column(db.String(200), nullable=False)

    def serialize(self):
         return {
             "id": self.id,
             "username": self.name,
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
    id = db.Column(db.Integer, primary_key=true) #Clave primaria de tabla
    label = db.Column(db.String(200))
    price = db.Column(db.String(200))

    def serialize(self):
         return {
             "id": self.id,
             "label": self.label,
             "price": self.price ,
         }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(seld):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()