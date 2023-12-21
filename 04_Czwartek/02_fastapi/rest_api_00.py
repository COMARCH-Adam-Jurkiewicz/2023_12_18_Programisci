import os
import uvicorn
from fastapi import FastAPI

__PORT__ = os.getenv("APP_PORT", 5500)
app = FastAPI()

if __name__ == "__main__":
    print(f"Start APP on port {__PORT__}")
    uvicorn.run(app, host="0.0.0.0", port=int(__PORT__))