import requests
import json


#class for abusIPDB
class Apioc:
    
    def __init__(self, endpoint, auth_token):
        self.endpoint = endpoint
        self.auth_token = auth_token

    def requisicao_para_x_ips(self, accept, method):
        querystring = {
            'ipAddress': '118.25.7.39',
            'maxAgeInDays': '90'
        }
        
        headers = {
            'Accept': f'{accept}',
            'Key': f'{self.auth_token}'
        }
        response = requests.request(method=method.upper(), url=self.endpoint, headers=headers, params=querystring)
        
        decodedResponse = json.loads(response.text)
        return decodedResponse
    
