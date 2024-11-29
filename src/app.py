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
def all_members():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()

    if members == []:
        return jsonify({"msg": "No hay miembreos"}), 404
    return jsonify(members), 200


# 2. Endpoint para recuperar un solo miembro de la familia
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        # Llamar al método get_member de la clase FamilyStructure
        member = jackson_family.get_member(member_id)
        
        # Si se encuentra el miembro, se devuelve como respuesta JSON
        if member:
            return jsonify(member), 200
        else:
            return jsonify({"message": "Member not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# 3. Endpoint para añadir miembros a la familia
@app.route('/member', methods=['POST'])
def add_member():
    try:
        request_body = request.json
        if not request_body:
            return jsonify({"message": "Request body is empty"}), 400

        if "first_name" not in request_body or "age" not in request_body or "lucky_numbers" not in request_body:
            return jsonify({"message": "Missing required fields: 'first_name', 'age', or 'lucky_numbers'"}), 400

        # Agregamos el nuevo miembro usando el método de la clase
        members = jackson_family.add_member(request_body)

        # Respuesta exitosa
        return jsonify(members, {"message": "Member added successfully"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# 4. Endpoint para eliminar un miembro de la familia
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    try:
        result = jackson_family.delete_member(id)
        if result:
            return jsonify({"done": True, "message": "Member deleted successfully"}), 200
        else:
            return jsonify({"message": "Member not found"}), 404
    except Exception as e:
        return jsonify({"message": int(e)}), 500
    
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
