from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

# Create app
app = FastAPI()

# Define user input schema
class User(BaseModel):
    email: EmailStr                      # Validates proper email format
    password: str = Field(..., min_length=6)   # Password must be at least 6 chars
    age: int = Field(..., gt=0, lt=150)        # Age must be between 1 and 149

# Route to create a user
@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully!",
        "user": user.dict()
    }

# Global error handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return {"error": "Something went wrong!", "details": str(exc)}

