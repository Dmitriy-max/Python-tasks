import requests
from requests.auth import HTTPBasicAuth
url = 'http://local00.zxteam.net:8332/'
credentials = HTTPBasicAuth('dev', 'erGmo1mU8jgGFf0FVWrTN4sL86Nwqdmw4oEQ9YTlVh8=')
payload = {"jsonrpc": "1.0", "id": "curltest", "method": "getblockhash", "params": [1000]}
response = requests.post(url, json = payload, auth = credentials)
#print(response.status_code)
print(response.json())