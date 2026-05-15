#coleta de dominios do hauss
from dotenv import load_dotenv
import requests
import os

class HaussApi:    
    
    def __init__(self, auth_token):
        self.auth_token = auth_token
    
    def getDomainList(self):
        url = f"https://urlhaus-api.abuse.ch/v2/files/exports/{self.auth_token}/hostfile.txt"
        response = requests.get(url)
        return response.text
    
    
load_dotenv()
api_key = os.getenv('API_KEY_HAUSS')
api_hauss = HaussApi(auth_token=api_key)
print(api_hauss.getDomainList())