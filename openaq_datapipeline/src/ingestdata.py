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
    dados = resposta.json()
    os.makedirs("data", exist_ok=True)
    with open("data/dados_brutos.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)