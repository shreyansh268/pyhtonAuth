import requests
from pprint import pprint

response = requests.get('https://api.github.com/users/{username}}', 
                        headers={'Authorization':'access_token {token}'})

pprint(response)