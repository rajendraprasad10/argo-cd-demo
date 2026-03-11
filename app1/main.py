# Approach:
# 1. Create FastAPI instance
# 2. Mount static files
# 3. Use Jinja2 templates
# 4. Render HTML page on "/"

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI(title="DevOps Rajendra Channel")

# Mount static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Template folder
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Home route renders channel info
    """
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "channel_name": "DevOps Rajendra",
            "description": "Learn Docker, Kubernetes, AWS, DevOps & Python in Telugu.",
            "author": "Rajendra Taidala"
        },
    )


@app.get("/health")
async def health_check():
    """
    Health check endpoint (Used in Kubernetes / Docker healthchecks)
    """
    return {"status": "OK"}

