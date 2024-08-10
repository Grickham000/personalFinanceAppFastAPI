# main.py
from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore
from controllers.UsersController import router as users_router

app = FastAPI()

# Initialize Firebase Admin SDK
cred = credentials.Certificate("personalfinance-a0728-firebase-adminsdk-vr1aa-aba9a3ab9e.json")
firebase_admin.initialize_app(cred)

# Include the routes from UsersController
app.include_router(users_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)