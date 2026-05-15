import requests
import json
from dotenv import load_dotenv
import os

#class for abusIPDB
class ApiIntegrations:
    
    #construtor
    def __init__(self, endpoint, auth_token):
        self.endpoint = endpoint
        self.auth_token = auth_token

    #coeleta de IPs do AbuseIPDB
    def abuseipdb_requisicao_coletaips(self):
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
    
    #coleta de dominios do hauss
    def hauss_requisicao_coletadomain(self):
        url = f"https://urlhaus-api.abuse.ch/v2/files/exports/{self.auth_token}/hostfile.txt"
        response = requests.get(url)
        return response.text
    
    def pihole_requisicao_adddomain_to_blocklist(self, domain, comment):
        payload = {'accept': 'application/json',
                'content-type': 'application/json',
                "password": f'{self.auth_token}',
                "domain": f'{domain}',
                "comment": f'{comment}',
                "groups": [0],
                "enabled": True}

        response = requests.request("POST", self.endpoint, json=payload, verify=False)
        print(response.text)



    
# load_dotenv()
# api_key = os.getenv('API_KEY_ABUSEIPDB')
# url = os.getenv('URL_ABUSEIPDB_BLACKLIST')
# api_adb = ApiAbuseIPDB(endpoint=url, auth_token=api_key)
# print(api_adb.requisicao_coleta_ips())


# load_dotenv()
# api_key = os.getenv('API_KEY_HAUSS')
# api_hauss = ApiIntegrations(endpoint=None, auth_token=api_key)
# print(api_hauss.hauss_requisicao_coletadomain())