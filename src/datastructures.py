
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "age": 33,
                "first_name": "John",
                "id": self._generateId(),
                "last_name": last_name,
                "lucky_numbers": [
                    7,
                    13,
                    22
                ]
            },
            {
                "age": 35,
                "first_name": "Jane",
                "id": self._generateId(),
                "last_name": last_name,
                "lucky_numbers": [
                    10,
                    14,
                    3
                ]
            },
            {
                "age": 5,
                "first_name": "Jimmy",
                "id": self._generateId(),
                "last_name": last_name,
                "lucky_numbers": [
                    1
                ]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    1# this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

    # 2. Endpoint para recuperar un miembro de la familia
    def get_member(self, id):
        # Busca el miembro con el id en la lista
        for member in self._members:
            if member["id"] == id:
                return member
        return None 

    # 3. Endpoint para añadir miembros a la familia
    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        if "last_name" not in member:
            member["last_name"] = self.last_name
        self._members.append(member)

    # 4. Endpoint para eliminar un miembro de la familia
    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True  # Retorna True si el miembro fue encontrado y eliminado
        return False 
    
