import requests
import json
import re

userPass = "teste"
convite = 123456
captchaAnswer = "ABC1"
celularSimSms = 11222334455
codigoSms = 88888
tokenSms = 88888
codeCap = 12345
timestamp = "data"

url = 'https://www.sssgame.com/api/member/register'
headers = {
    'Host': 'www.sssgame.com',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium;v="114", Google Chrome";v="114"',
    'language': 'pt',
    'sec-ch-ua-mobile': '?0',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Context-Type': 'application/json;charset-UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'device': 'Pc',
    'sign': 'c2294354d3494b319f73ca333d293a4a',
    'sec-ch-ua-platform': 'Windows',
    'Origin': 'https://www.sssgame.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.sssgame.com/',
    'Cookie': ''
}

data = {
    "username": userPass,
    "password": userPass,
    "confirmPassword": userPass,
    "realName": "",
    "mobile": celularSimSms,
    "spreaderId": convite,
    "verifyCode": captchaAnswer,
    "birthday": "2023-07-19",
    "email": "",
    "fistNAme": "",
    "lastName": "",
    "areaCode": "55",
    "mobileCode": codigoSms,
    "emailCode": "",
    "uuid": tokenSms,
    "verificationCode": codeCap,
    "identificationType": "CPF",
    "identificationNumber": "",
    "identificationCode": 4,
    "timestamp": timestamp
}
data_json = json.dumps(data)

proxy_url = 'https://pr.pyproxy.com:16666'
proxy_auth = ('TropaZ01-zone-resi-region-br', '102030Paz')

try:
    response = requests.post(
        url,
        json=data_json,
        headers=headers,
        proxies={'https': proxy_url},
        auth=proxy_auth  # Potential issue with this line
    )

    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

r2 = response.text

def pegarMensagem(response_text):
    pattern = r'msg" : "(.*?)"'
    match = re.search(pattern, response_text)
    match.group(1) if match else None

msgfinal = pegarMensagem(r2)

print(msgfinal)


