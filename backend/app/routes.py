from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
  return {"message": "Hello from FastAPI Router"}

@router.get("/test")
def test(): 
  return {"message": "Test API."}