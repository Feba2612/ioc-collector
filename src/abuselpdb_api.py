import requests
import json
from dotenv import load_dotenv
import os

#class for abusIPDB
class ApiAbuseIPDB:
    #construtor
    def __init__(self, endpoint, auth_token):
        self.endpoint = endpoint
        self.auth_token = auth_token

    #método para payload
    def requisicao_coleta_ips(self):
        querystring = {
            'limit' : '10000',
            'ipVersion': 4
        }
        
        headers = {
            'Accept': 'text/plain',
            'Key': f'{self.auth_token}'
        }
        response = requests.request(method='GET', url=self.endpoint, headers=headers, params=querystring)
        
        return response.text


    
# load_dotenv()
# api_key = os.getenv('API_KEY_ABUSEIPDB')
# url = os.getenv('URL_ABUSEIPDB_BLACKLIST')
# api_adb = ApiAbuseIPDB(endpoint=url, auth_token=api_key)
# print(api_adb.requisicao_coleta_ips())
