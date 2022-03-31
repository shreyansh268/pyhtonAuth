import requests
from requests.auth import HTTPBasicAuth

response = requests.get('https://api.github.com/users/', 
                        auth=HTTPBasicAuth('user', 'pass'))

print(response)