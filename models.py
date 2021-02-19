from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=true) #Clave primaria de tabla
    name = db.Column(db.String(100), nulleable=False)
    last_name = db.Column(db.String(100), nulleable=False)
    email = db.Column(db.String(100), nulleable=False, unique=True)
    phone = db.Column(db.String(100), nulleable=False)

    def serialize(self):
         return {
             "id": self.id,
             "name": self.name,
             "last_name": self.last_nae,
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