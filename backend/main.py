from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Vidhitam Chakole Portfolio API")

allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactMessage(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    message: str = Field(min_length=1, max_length=2000)

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
