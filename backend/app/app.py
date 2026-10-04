from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(): 
  return get_message()

def get_message(): 
  return {"message": "Test endpoint."}