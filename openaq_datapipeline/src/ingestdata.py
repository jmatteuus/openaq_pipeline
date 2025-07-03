import requests
import os
import json

url = "https://api.openaq.org/v3/locations"

parametros_requisicao = {
    "country": "Brasil",
    "limit": 100,
    "page": 5

}

headers = {
    "X-API-Key": os.getenv("API_KEY")
}

resposta = requests.get(url, params=parametros_requisicao, headers=headers)