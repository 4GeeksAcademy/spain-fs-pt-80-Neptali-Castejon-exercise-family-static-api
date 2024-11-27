
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

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    1# this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members


    # 2. Endpoint para recuperar un miembro de la familia
    def get_member(self, id):
        pass

    # 3. Endpoint para añadir miembros a la familia
    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        if "last_name" not in member:
            member["last_name"] = self.last_name
        self._members.append(member)

    # 4. Endpoint para eliminar un miembro de la familia
    def delete_member(self, id):
        pass


    
