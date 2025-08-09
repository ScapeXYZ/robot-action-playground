## Quick Start

## Repository Structure

robot-action-playground/ │ ├── websim/ │   ├── init.py                 # Makes websim a Python package │   ├── app.py                      # FastAPI app entry point │   └── templates/ │       └── playground.html         # Robot Action Playground UI │ ├── requirements.txt                # Project dependencies ├── README.md                       # Project documentation └── .env.example                    # Example environment variables (OM1 API key)







# 🤖 Robot Action Playground

A tiny web app that simulates robot actions (Speak, Move, Smile) using the **OpenMind OM1 API.** Runs locally in the browser—no physical robot required.

## Quick Start (no Docker)
1. Install Python 3.10+.
2. Install deps (see requirements.txt).
3. Set your OM1 key:
   - Linux/macOS: export OM1_API_KEY="om1_live_..."
   - Windows (PowerShell): $env:OM1_API_KEY="om1_live_..."
4. Run:

`uvicorn websim.app:app --host 0.0.0.0 --port 8000`

5. Open http://localhost:8000/playground.

## What it does
- Sends your task to OM1 chat completions
- Requests a small JSON plan like:
`json
{"actions":[{"type":"speak","text":"Hello!"}]}

Simulates the actions with a speech bubble, emoji smile, and simple movement.


## Screenshot
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/1b23f622-ea4d-4dcb-bd3a-f7d6b5179c3b" />
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/f28fe4f6-5da9-466d-8941-b61f33c6d495" />
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/ef927a56-5a94-4c8e-91cd-616419d797d7" />
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/51c52f2d-089f-418b-8b9a-b9ba6d48bd6d" />



Credits

Built with ❤️ on top of OpenMind/OM1. Licensed MIT.

---

### 3) Commit each file
At the bottom of the editor:
- Write a short message (e.g., `add websim app + playground`).
- Choose Commit directly to main.
- Click Commit changes.

Repeat for all files above.

---

### 4) Upload your screenshot
- Click Add file → Upload files.
- Drag your screenshot (e.g., `screenshot.png`) and Commit changes.
- Edit `README.md` and link it:  
  `![Playground]
  <img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/2191872c-c838-456a-876b-c734c519d14a" />


---

### 5) How to run (for readers)
They only need to:
- Install requirements  
- Set `OM1_API_KEY`  
- Run uvicorn  
- Visit `/playground`

If you want, I can also add a Dockerfile or GitHub Codespaces button later—totally no-CLI for your users.0
