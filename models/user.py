from pydantic import BaseModel

class User(BaseModel):
    email: str
    nombre: str
    password: str
    role: str

    # Optionally, you can add methods to manipulate or validate the data
    def is_valid(self):
        # Example validation method
        return all([self.email, self.nombre, self.password, self.role])
    
    def to_dict(self):
        return {
            "email": self.email,
            "nombre": self.nombre,
            "password": self.password,
            "role": self.role
        }
