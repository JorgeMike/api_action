from flask import Flask, jsonify

# Crear la aplicación Flask
app = Flask(__name__)

# Endpoint 1: Información de un usuario
@app.route('/api/usuario', methods=['GET'])
def get_usuario():
    usuario = {
        "id": 1,
        "nombre": "Juan Pérez",
        "edad": 30,
        "email": "juan@example.com"
    }
    return jsonify(usuario)  # Retorna el diccionario como JSON

# Endpoint 2: Lista de productos
@app.route('/api/productos', methods=['GET'])
def get_productos():
    productos = [
        {"id": 1, "nombre": "Laptop", "precio": 1200.50},
        {"id": 2, "nombre": "Mouse", "precio": 25.00},
        {"id": 3, "nombre": "Teclado", "precio": 45.75}
    ]
    return jsonify(productos)  # Retorna la lista como JSON

# Endpoint 3: Estado del servidor
@app.route('/api/estado', methods=['GET'])
def get_estado():
    estado = {
        "servidor": "activo",
        "version": "1.0.0",
        "timestamp": "2025-03-04T12:00:00Z"
    }
    return jsonify(estado)  # Retorna el estado como JSON

# Configuración para ejecutar la API
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)