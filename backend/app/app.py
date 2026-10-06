from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  return {"message": "Test endpoint"}

@app.post("/")
def test_post():
  return {"message": "Test post endpoint"}
