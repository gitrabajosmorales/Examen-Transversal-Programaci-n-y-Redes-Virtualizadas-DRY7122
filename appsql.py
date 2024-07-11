from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definición del modelo de usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'

# Crear la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# Ruta para crear un nuevo usuario
@app.route('/registrar', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    nombre = data.get('nombre')
    password = data.get('password')

    if not nombre or not password:
        return jsonify({'message': 'Nombre y contraseña son requeridos'}), 400

    # Hash de la contraseña
    password_hash = generate_password_hash(password)
    
    nuevo_usuario = Usuario(nombre=nombre, password_hash=password_hash)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'message': 'Usuario registrado exitosamente'}), 201

# Ruta para validar un usuario
@app.route('/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    nombre = data.get('nombre')
    password = data.get('password')

    usuario = Usuario.query.filter_by(nombre=nombre).first()
    if usuario and check_password_hash(usuario.password_hash, password):
        return jsonify({'message': 'Inicio de sesión exitoso'}), 200
    else:
        return jsonify({'message': 'Nombre o contraseña incorrectos'}), 401

# Ejecutar la aplicación en el puerto 5800
if __name__ == '__main__':
    app.run(port=5800)
