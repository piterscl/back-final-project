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
manager.add_command('db', MigrateCommand)  #init migrate y el upgrade

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/login", methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username: return jsonify({"msg": "nombre de es requerido"}), 400
    if not password: return jsonify({"msg": "password is required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user: return jsonify({"msg": "username/password are incorrect!!!"}), 400
    

    if not check_password_hash(user.password, password):
        return jsonify({"msg": "username/password are incorrect!!!"}), 400
    
    expires = datetime.timedelta(days=1)

    access_token = create_access_token(identity=user.id, expires_delta=expires)

    data = {
        "access_token": access_token,
        "user": user.serialize()
    }

    return jsonify(data), 200

@app.route("/Registro", methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username: return jsonify({"msg": "username is required"}), 400
    if not password: return jsonify({"msg": "password is required"}), 400

    user = User.query.filter_by(username=username).first()
    if user: return jsonify({"msg": "username already exists!!!"}), 400
    
    user = User()
    user.username = username
    user.password = generate_password_hash(password)
    user.save()

    if not user: return jsonify({"msg": "Register Failed!!!"}), 400

    expires = datetime.timedelta(days=3)

    access_token = create_access_token(identity=user.id, expires_delta=expires)

    data = {
        "access_token": access_token,
        "user": user.serialize()
    }

    return jsonify(data), 200


@app.route("/perfil", methods=['GET'])
@jwt_required()
def profile():
    id = get_jwt_identity()
    user = User.query.get(id)
    return jsonify(user.serialize()), 200

if __name__ == '__main__':
    manager.run()