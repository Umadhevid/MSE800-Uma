from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# Serve static HTML
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_home():
    with open("static/temperature_converter.html", "r") as f:
        return f.read()

# Conversion model
class ConversionRequest(BaseModel):
    value: float
    conversion_type: str

@app.post("/convert")
async def convert_temperature(req: ConversionRequest):
    v = req.value
    t = req.conversion_type
    result = None

    if t == "CtoF": result = v * 9/5 + 32
    elif t == "FtoC": result = (v - 32) * 5/9
    elif t == "CtoK": result = v + 273.15
    elif t == "KtoC": result = v - 273.15
    elif t == "FtoK": result = (v - 32) * 5/9 + 273.15
    elif t == "KtoF": result = (v - 273.15) * 9/5 + 32
    else: return JSONResponse(content={"error": "Invalid conversion type"}, status_code=400)

    return {"converted": round(result, 2)}
