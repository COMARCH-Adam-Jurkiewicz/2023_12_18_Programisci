import requests
import json

link = 'http://127.0.0.1:5500/'

r = requests.get(link+"auth/TEST-OK")
dane = r.json()

print(json.dumps(dane, indent=2, ensure_ascii=False))