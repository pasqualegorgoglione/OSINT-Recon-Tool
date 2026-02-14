import requests

def checkDomain(domain, api_key):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    headers = {"accept": "application/json",
              "x-apikey": api_key}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[!]Error API Status. Error status: {response.status_code} for domain: {domain}")
    except Exception as e:
        print(f"[!]Critical error: {e}")
        return ""    

   