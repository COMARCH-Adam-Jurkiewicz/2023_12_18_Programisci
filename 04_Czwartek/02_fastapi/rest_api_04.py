from fastapi import FastAPI
import uvicorn
import os
from urllib.parse import parse_qs

__PORT__ = os.getenv("APP_PORT", 5500)
app = FastAPI()

@app.get("/items/{q}")
async def read_items(q: str = None):
    if q:
        params = parse_qs(q)
        return {"q": q, "params": params}
    return {"q puste": q}

if __name__ == "__main__":
    print(f"Start APP on port {__PORT__}")
    uvicorn.run(app, host="0.0.0.0", port=int(__PORT__))