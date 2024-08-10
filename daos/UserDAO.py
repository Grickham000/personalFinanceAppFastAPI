# daos/UserDAO.py
from firebase_admin import firestore

class UserDAO:
    def __init__(self, db):
        self.db = db

    def get_user(self, email: str):
        doc_ref = self.db.collection('Users').document(email)
        doc = doc_ref.get()
        if not doc.exists:
            return None
        return doc.to_dict()
    
    def get_all_users(self):
        users = []
        for doc in self.db.collection('Users').stream():
            users.append(doc.to_dict())
        return users

    def save_user(self, email: str, user_data: dict):
        doc_ref = self.db.collection('Users').document(email)
        doc_ref.set(user_data)

    def update_user(self, email:str, user_data:dict):
        doc_ref = self.db.collection('Users').document(email)
        doc_ref.set(user_data)

    def delete_user(self, email: str):
        doc_ref = self.db.collection('Users').document(email)
        doc_ref.delete()