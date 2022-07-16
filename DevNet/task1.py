import requests
import sys
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

def get_auth_token():
    login_url = "https://sandboxdnac.cisco.com:443/api/system/v1/auth/token"
    result = requests.post(url=login_url, auth=HTTPBasicAuth("devnetuser", "Cisco123!"), verify=False)
    result.raise_for_status()

    token = result.json()["Token"]
    return {
        "controller_ip": "sandboxdnac.cisco.com",
        "token": token
    }

def get_device_info():
    url = "https://sandboxdnac.cisco.com:443/api/v1/network-device"
    token = get_auth_token()
    headers = {'X-auth-token' : token['token']}
    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as cerror:
        print("Error processing request", cerror)
        sys.exit(1)
    return response.json()