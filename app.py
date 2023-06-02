from fastapi import FastAPI
import uvicorn
import requests


app = FastAPI()


@app.get("/")
def read_root():
    r = requests.get('https://api.gameofthronesquotes.xyz/v1/random').json()
    quote = r['sentence']
    character = r['character']['name']
    return {'result': f"{character} : {quote}"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
