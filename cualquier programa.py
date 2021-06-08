import requests
import urllib3
import json

ip_address = '192.168.1.50'
interface = 'loopback1'
username = 'cisco'
password = 'cisco'

def get_token():
    """
    Autenticar y obtener token
    """

    url = 'https://%s:55443/api/v1/auth/token-services' % ip_address
    auth = (username, password) 
    headers = {'Content-Type':'application/json'}
    response = requests.post(url, auth=auth, headers=headers, verify=False)
    json_data = json.loads(response.text)
    token = json_data['token-id']
    print('We received token: %s' % token)
    return token

def put_interface(token, interface):
    """
    Obtener información de la interfaz del router.
    """
    url = 'https://%s:55443/api/v1/interfaces/%s' % (ip_address, interface)
    headers={ 'Content-Type': 'application/json', 'X-auth-token': token}

    payload = {
        'type':'ethernet',
        'if-name':interface,
        'ip-address':'11.11.11.11',
        'subnet-mask':'255.255.255.255',
        'description': 'TEST-PUT-INTERFACE'
        }

    response = requests.put(url, headers=headers, json=payload, verify=False)
    print('El router responde de esta manera: %s ' % response.status_code)


# Disable unverified HTTPS request warnings.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get token.
token = get_token()

# PUT interface information.
put_interface(token, interface)
