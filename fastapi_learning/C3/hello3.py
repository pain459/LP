# Using query parameters
from fastapi import FastAPI

app = FastAPI()


@app.get("/hi")
def greet(who):
    return f'Hello {who}?'


@app.get("/snape")
def snape(name):
    return f'Page no. 269.'


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("hello3:app", reload=True)
