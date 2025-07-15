from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "result": None})

@app.post("/", response_class=HTMLResponse)
def calculate(request: Request, a: float = Form(...), b: float = Form(...)):
    result = {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": "Infinity" if b == 0 else a / b
    }
    return templates.TemplateResponse("form.html", {"request": request, "result": result, "a": a, "b": b})
 
