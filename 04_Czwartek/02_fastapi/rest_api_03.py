import os
import uvicorn
from fastapi import FastAPI, HTTPException, Request, status, Response

__PORT__ = os.getenv("APP_PORT", 5500)
app: FastAPI = FastAPI()

# endpoint w api
@app.get("/")
def fn_main():
    return {"opis": "nic nie zwracamy"}

@app.get("/auth/{auth_id}")
def fn_auth(request: Request,
            auth_id: str):
    if not auth_id == "TEST-OK":
        # mówimy, że źle
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail=f"AUTH Error for {auth_id} from {request.client.host}")

    return {"informacja": "Połączenie poprawne"}

@app.get("/auth/v2/{auth_id}", status_code=status.HTTP_202_ACCEPTED)
def fn_auth(request: Request,
            response: Response,
            auth_id: str):
    if not auth_id == "TEST-OK":
        # mówimy, że źle
        response.status_code = status.HTTP_410_GONE
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail=f"AUTH Error for {auth_id} from {request.client.host}")

    return {"informacja": "Połączenie poprawne"}

@app.get("/auth/v3/{auth_id}", status_code=status.HTTP_202_ACCEPTED)
def fn_auth(request: Request,
            response: Response,
            auth_id: str):
    """X-Header Authentication"""
    print(request.headers)
    auth_id_x = request.headers.get("auth_id", "no_x_id")
    print(auth_id_x)
    if not auth_id == "TEST-OK":
        # mówimy, że źle
        response.status_code = status.HTTP_410_GONE
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail=f"AUTH Error for {auth_id} from {request.client.host}")

    return {"informacja": "Połączenie poprawne"}


if __name__ == "__main__":
    print(f"Start APP on port {__PORT__}")
    uvicorn.run(app, host="0.0.0.0", port=int(__PORT__))