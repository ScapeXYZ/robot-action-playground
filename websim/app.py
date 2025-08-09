import os, requests
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="OM1 Web Simulator")
BASE_DIR = Path(file).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

CHAT_URL = "https://api.openmind.org/api/core/openai/chat/completions"

def get_api_key():
    return os.environ.get("OM1_API_KEY")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/playground", response_class=HTMLResponse)
async def playground(request: Request):
    return templates.TemplateResponse("playground.html", {"request": request})

@app.post("/playground/run")
async def run_playground(request: Request):
    api_key = get_api_key()
    if not api_key:
        return JSONResponse({"error": "OM1_API_KEY not set"}, status_code=400)

    data = await request.json()
    task = data.get("task", "Say hello")
    actions_enabled = set(data.get("actions", []))

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    system = (
        "You control a simple simulated robot. "
        "Output STRICT JSON only matching this schema: "
        '{"actions":[{"type":"speak","text":"..."},'
        '{"type":"move","motion":"walk","distance_m":float},'
        '{"type":"smile","intensity":"small|big"}]} '
        "Only use types the client enabled: " + ", ".join(sorted(actions_enabled or {"speak"})) + "."
    )
    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": f"Task: {task}. Return only JSON."}
        ]
    }
    r = requests.post(CHAT_URL, headers=headers, json=payload, timeout=30)
    j = r.json()

    try:
        content = j["choices"][0]["message"]["content"]
        import json as pyjson
        actions = pyjson.loads(content).get("actions", [])
    except Exception:
        actions = [{"type": "speak", "text": "Hello!"}]

    actions = [a for a in actions if a.get("type") in actions_enabled or not actions_enabled]
    return {"actions": actions, "raw": j}
