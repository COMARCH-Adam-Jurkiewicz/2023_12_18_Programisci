import os
import uvicorn
from fastapi import FastAPI, HTTPException, Request

__PORT__ = os.getenv("APP_PORT", 5500)
app: FastAPI = FastAPI()

# endpoint w api
@app.get("/")
async def fn_main():
    return {"opis": "nic nie zwracamy"}

@app.get("/auth/{auth_id}")
def fn_auth(request: Request,
            auth_id: str):
    if not auth_id == "TEST-OK":
        # mówimy, że źle
        return HTTPException(status_code=401,
                             detail=f"AUTH Error for {auth_id} from {request.client.host}")

    return {"informacja": f"Połączenie poprawne from {request.client.host}"}


if __name__ == "__main__":
    print(f"Start APP on port {__PORT__}")
    uvicorn.run(app, host="0.0.0.0", port=int(__PORT__))