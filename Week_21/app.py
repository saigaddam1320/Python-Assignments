from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="Week 21 - Validation & Error Handling")

class User(BaseModel):
    email: EmailStr
    age: int = Field(gt=0, lt=151)
    name: str = Field(min_length=1, max_length=50)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/users")
def create_user(user: User):
    return {"message": "user created", "data": user.dict()}

@app.exception_handler(RequestValidationError)
async def on_validation_error(request: Request, exc: RequestValidationError):
    errors = [{"field": ".".join(map(str, e["loc"])), "error": e["msg"]} for e in exc.errors()]
    return JSONResponse(status_code=422, content={"success": False, "errors": errors})

@app.exception_handler(Exception)
async def on_any_error(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"success": False, "error": "Internal server error"})
