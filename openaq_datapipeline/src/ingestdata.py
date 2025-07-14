import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

url = "https://api.openaq.org/v3/locations"

parametros_requisicao = {
    "country": "BR",
    "limit": 100,
    "page": 5

}

headers = {
    "X-API-Key": os.getenv("API_KEY")
}

resposta = requests.get(url, params=parametros_requisicao, headers=headers)

if resposta.status_code == 200:
    print('OK')
else:
    print(f'Verificar: {resposta.status_code}')