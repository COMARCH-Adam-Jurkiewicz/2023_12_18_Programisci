import requests

def check_web_page(adrress: str):
    scan_url = f"https://urlscan.io/api/v1/search/?q=filename:{adrress}"

    r = requests.get(scan_url)

    if r.status_code == 200:
        dane = r.json()
        result = dane['result']
        return result
    return "xxxxxxxxxxxxx"
