import requests
import re

def PegarIp(response_text):
    pattern = r'Meu ip é\s*([\d.]+)'
    match = re.search(pattern, response_text)
    if match:
        return match.group(1)
    return None

url = 'https://meuIp.com.br'

headers = {
    'Host': 'meuip.com.br',
    'Connection': 'keep-alive',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/avif, image/webp, image/apng, */*;q=0.8, application/signed-exchange;v=b3;q=0.7'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    meuIp = PegarIp(response.text)
    if meuIp:
        print(f"Meu endereço de IP: {meuIp}")
    else:
        print("IP não encontrado")
else:
    print(f"Falha na requisição: {response.status_code}")
