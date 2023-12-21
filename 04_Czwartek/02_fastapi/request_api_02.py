import requests

url = "http://127.0.0.1:5500"

docs = f"{url}/docs"
auth2 = f"{url}/auth/v2"
auth2_err = f"{auth2}/TEST-ERR"
auth2_ok = f"{auth2}/TEST-OK"

req_1 = requests.get(auth2_ok)
print(req_1.text)
print(req_1.status_code)