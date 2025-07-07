from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import yt_dlp
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/download")
async def download(song: str):
    output_path = "song.mp3"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'noplaylist': True,
        'default_search': 'ytsearch',
        'cachedir': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song])

    return FileResponse(output_path, media_type='audio/mpeg', filename="song.mp3")
