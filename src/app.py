"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }
    return jsonify(response_body), 200




# 2. Endpoint para recuperar un solo miembro de la familia



# 3. Endpoint para añadir miembros a la familia
@app.route('/members', methods=['POST'])
def add_member():
    try:
        body = request.get_json()
        if not body:
            return jsonify({"message": "Request body is empty"}), 400

        if "first_name" not in body or "age" not in body or "lucky_numbers" not in body:
            return jsonify({"message": "Missing required fields: 'first_name', 'age', or 'lucky_numbers'"}), 400

        # Agregamos el nuevo miembro usando el método de la clase
        jackson_family.add_member(body)

        # Respuesta exitosa
        return jsonify({"message": "Member added successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500



# 4. Endpoint para eliminar un miembro de la familia



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
