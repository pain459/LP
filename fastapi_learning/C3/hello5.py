# passing the greeting argument as HTTP header
from fastapi import FastAPI, Header

app = FastAPI()

@app.post("/hi")
def greet(who:str = Header()):
    return f'Hello? {who}'


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello5:app", reload=True)