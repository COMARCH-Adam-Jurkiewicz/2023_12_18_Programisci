from fastapi import FastAPI
import uvicorn
import os
from urllib.parse import parse_qs

__PORT__ = os.getenv("APP_PORT", 5500)
app = FastAPI()

@app.get("/items/")
async def read_items(q: str = None, liczba: int = 0):
    if q:
        params = parse_qs(q)
        return {"q": q, "params": params}
    return {"full": q, "l": liczba}

@app.get("/elems/") # http://0.0.0.0:5500/elems/?q=cosik&l=10
async def read_elems(q: str = None, l: int = 0):
    return {"co": q, "ile": l, "max": (l * 3)}

@app.get("/elemt/{q}/")  # http://0.0.0.0:5500/elemt/cosik/?l=10
# http://0.0.0.0:5500/elemt/cosik/?q=dddd&l=10
async def read_elems(q: str = None, l: int = 0):
    return {"cot": q, "ile": l, "max": (l * 3)}

@app.put("/eleml/{q}/")  # http://0.0.0.0:5500/elemt/cosik/?l=10
# http://0.0.0.0:5500/elemt/cosik/?q=dddd&l=10
async def read_eleml(q: str = None, l: list[int] = None):
    return {"cot": q, "lista": l}


if __name__ == "__main__":
    print(f"Start APP on port {__PORT__}")
    uvicorn.run(app, host="0.0.0.0", port=int(__PORT__))