from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Vidhitam Chakole Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactMessage(BaseModel):
    name: str
    message: str

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Backend is running"}

@app.post("/api/contact")
def send_contact(contact: ContactMessage):
    # This will be implemented to send an email or store in Supabase
    return {"status": "success", "message": "aajayega tode der me reply"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
