import requests
from dotenv import load_dotenv
import os

class PiHoleApi:
    
    def __init__(self, endpoint, auth_token):
        self.endpoint = endpoint
        self.auth_token = auth_token

    def auth(self):
        
        payload = {'accept': 'application/json',
                    'content-type': 'application/json',
                    'password':' '} 
        
        load_dotenv()
        url = os.getenv('URL_PIHOLE_AUTH')
        response = requests.request("POST", url, json=payload, verify=False)
        
        #TODO: A autenticação do Pihole retorna um SID, que é necessário para realizar outras requisições. O método auth() deve retornar esse SID para ser utilizado posteriormente.
        sid = response.json()
        return response.json

 
    #Adiciona dominio na blocklist do PiHole (FALTA TESTAR)
    def setDomainToBlocklist(self, domain, comment):
        bearer_token = self.auth()
        payload = {'accept': 'application/json',
                   'sid': f'{bearer_token}',
                'content-type': 'application/json',
                "password": f'{self.auth_token}',
                "domain": f'{domain}',
                "comment": f'{comment}',
                "groups": [0],
                "enabled": True}

        response = requests.request("POST", self.endpoint, json=payload, verify=False)
        print(response.text)


# load_dotenv()
# api_key = os.getenv('API_KEY_PIHOLE')
# endpoint = os.getenv('URL_PIHOLE_BLOCK_DOMAIN')
# api_piHole = PiHoleApi(endpoint=endpoint, auth_token=api_key)
# print(api_piHole.auth())
# #print(api_piHole.setDomainToBlocklist(domain="example.com", comment="Test domain"))