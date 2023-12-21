import requests
import json

def check_web_page(adrress: str):
    scan_url = f"https://urlscan.io/api/v1/search/?q=filename:{adrress}"

    r = requests.get(scan_url)

    if r.status_code == 200:
        dane = r.json()["results"][0]
        # print(f"{type(dane)} | {dane=}")
        dane_res = dane["result"]
        # print(f"---> {type(dane_res)} | {dane_res=}")
        # for klucz in dane:
        #     print(f"{type(klucz)} | {klucz=}")
        #     print(f"{dane[klucz]=}")
        #     print("---------")
            # print(json.dumps(dane, indent=2))
        # result = dane['result']
        return dane_res
    return "xxxxxxxxxxxxx"

if __name__ == "__main__":
    print(check_web_page("blog.jurkiewicz.tech"))
    print(check_web_page("wp.pl"))
    print(check_web_page("tozipxc6.dreamwp.com"))
    print(check_web_page("tozipxc6.dreamwp.com/wp-content/ih/ilo/mo/home/info.php"))