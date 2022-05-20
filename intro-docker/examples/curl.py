import sys, json, requests

if len(sys.argv) < 3:
    print(f"expected 2 arguments: METHOD URL, got {len(sys.argv)}.")
    exit()

method,url = sys.argv[1:3]

# Defined by requests.request
methods = {
    "GET", "POST", "PUT", "PATCH", 
    "DELETE", "HEAD", "OPTIONS"
}

if method.upper() not in methods:
    print(f"invalid method {method}, please select another method.")
    exit()

if not url.startswith("http") and "://" not in url:
    url = "http://" + url

resp = requests.request(method=method, url=url)
print(json.dumps(resp.json(), indent=4))