import os
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, jsonify
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from models import db, User, Servicios, Horarios, Extras
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = os.getenv('DEBUG')
app.config['ENV'] = os.getenv('ENV')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

db.init_app(app)
jwt = JWTManager(app)
Migrate(app, db)
CORS(app)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.route("/")
def main():
    return render_template('index.html')

#Login
@app.route("/Login", methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username: return jsonify({"msg": "username es requerido"}), 400
    if not password: return jsonify({"msg": "contraseña es requerida"}), 400

    user = User.query.filter_by(username=username).first()
    if not user: return jsonify({"msg": "username/contraseña incorrectos"}), 400
    

    if not check_password_hash(user.password, password):
        return jsonify({"msg": "nombre/contraseña incorrectos"}), 400
    
    expires = datetime.timedelta(days=1)

    access_token = create_access_token(identity=user.id, expires_delta=expires)

    data = {
        "access_token": access_token,
        "user": user.serialize()
    }

    return jsonify(data), 200

#/Registro
@app.route("/Registro", methods=['POST'])
def register():
    username = request.json.get('username')
    apellido = request.json.get('apellido')
    password = request.json.get('password')
    email = request.json.get('email')
    phone = request.json.get('telefono')

    if not username: return jsonify({"msg": "username es requiredo"}), 400
    if not apellido: return jsonify({"msg": "apellido es requiredo"}), 400
    if not password: return jsonify({"msg": "contraseña es requireda"}), 400
    if not email: return jsonify({"msg": "email es requiredo"}), 400
    if not phone: return jsonify({"msg": "telefono es requiredo"}), 400

    user = User.query.filter_by(email=email).first()
    if user: return jsonify({"msg": "el email ya se encuentra registrado"}), 400
    
    user = User()
    user.username = username
    user.password = generate_password_hash(password)
    user.apellido = apellido
    user.email = email
    user.phone = phone
    user.save()

    if not user: return jsonify({"msg": "Falló registro"}), 400

    expires = datetime.timedelta(days=1)

    access_token = create_access_token(identity=user.id, expires_delta=expires)

    data = {
        "access_token": access_token,
        "user": user.serialize()
    }

    return jsonify(data), 200

#/Profile
@app.route("/Profile", methods=['GET'])
@jwt_required()
def profile():
    id = get_jwt_identity()
    user = User.query.get(id)
    return jsonify(user.serialize()), 200

#/Servicios
@app.route("/API/Servicios", methods=['POST'])
def crearServicio():
    servicio_id = request.json.get('servicio_id')
    nombre_servicio = request.json.get('nombre_servicio')
    valor_servicio = request.json.get('valor_servicio')

    if not servicio_id: return jsonify({"msg": "id es requerido"}), 400
    if not nombre_servicio: return jsonify({"msg": "nombre servicio es requerido"}), 400
    if not valor_servicio: return jsonify({"msg": "valor servicio es requerido"}), 400

    servicio = Servicios.query.filter_by(servicio_id=servicio_id).first()
    if servicio: return jsonify({"msg": "el id ya se encuentra en uso"}), 400
    
    servicio = Servicios()  
    servicio.servicio_id = servicio_id
    servicio.nombre_servicio = nombre_servicio
    servicio.valor_servicio = valor_servicio
    servicio.save()

    if not servicio: return jsonify({"msg": "Falló registro"}), 400

    data = {
        "servicio": servicio.serialize()
    }

    return jsonify(data), 200

#/Extras
@app.route("/API/Extras", methods=['POST'])
def crearExtras():
    extras_id = request.json.get('extras_id')
    nombre_extra = request.json.get('nombre_extra')
    valor_extra = request.json.get('valor_extra')

    if not extras_id: return jsonify({"msg": "id extra es requerido"}), 400
    if not nombre_extra: return jsonify({"msg": "nombre extra es requerido"}), 400
    if not valor_extra: return jsonify({"msg": "valor extra es requerido"}), 400

    extra = Extras.query.filter_by(extras_id=extras_id).first()
    if extra: return jsonify({"msg": "el id ya se encuentra en uso"}), 400
    
    extra = Extras()  
    extra.extras_id = extras_id
    extra.nombre_extra = nombre_extra
    extra.valor_extra = valor_extra
    extra.save()

    if not extra: return jsonify({"msg": "Falló registro"}), 400

    data = {
        "extras": extra.serialize()
    }

    return jsonify(data), 200

if __name__ == '__main__':
    manager.run()