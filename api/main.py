from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import src.spotify

app = FastAPI()

class PlaylistConstructor(BaseModel):
    name : str
    text : str
    access_token : str

@app.get("/")
def read_main():
    return "Welcome to Sounday API!", 200

@app.post("/playlist/")
async def read_playlist(client_playlist : PlaylistConstructor):
    return playlist(client_playlist.access_token, client_playlist.text, client_playlist.title)

