import requests
import json
import re
import time
import random

def echoAndFlush(msg):
    print(msg)
    import sys
    sys.stdout.flush()

url = 'https://simsms.org/reg-sms.api.php?type=get_number&country_id=BR&operator=Total_BR&service=opt19&id=1&redirectphone=0'
headers = {
    'Host': 'simsms.org',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Cookie': '_ym_uid=1689721572528725105; _ym_d=1689721572; _ym_isad=1; supportOnlineTalkID=1pDDRDN1540gQMssPcTScTFXyL0H1JzM; PHPSESSID=jc055av4vcmkj5vlrlqp05udh; dle_user_id=319631; dle_password=82ce70275707c7cccb0310923aeff296; dle_newpm=0; _ym_visorc=w'
}

response = requests.get(url, headers=headers)
final = response.text

split_string = final.split("~")

celularsimsms = split_string[1]
idsms = split_string[2]

if 'error' in final:
    echoAndFlush("Ocorreu algum erro ao gerar seu número na plataforma, provavelmente seu token expirou.<br>")

number = 1689788237022
min_number = 10 ** (len(str(number)) - 1)
max_number = (10 ** len(str(number))) - 1
timestamp = str(random.randint(min_number, max_number))

url = 'https://www.sssgame.com/api/member/sendCode'
headers = {
    'Host': 'www.sssgame.com',
    'Connection': 'keep-alive',
    'language': 'pt',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Context-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'device': 'Pc',
    'sign': '',
    'Cookie': ''
}
data = {
    "email": "",
    "areaCode": "+55",
    "mobile": celularsimsms,
    "item": 1,
    "timestamp": timestamp
}
data_json = json.dumps(data)

response = requests.post(url, data=data_json, headers=headers)
response_data = response.json()
msgsms = response_data.get('msg', '')
tokensms = response_data.get('data', '')

# Check if the SMS was sent successfully
sucessMessage = "Código de verificação enviado com sucesso"
maxAttempts = 3

for attempts in range(1, maxAttempts + 1):
    if sucessMessage in msgsms:
        echoAndFlush("SMS enviado com sucesso, script em execução. Aguardando 60 segundos para verificar se o SMS chegou.")
        time.sleep(60)

        # Get SMS verification code
        url = f'https://simsms.org/reg-sms.api.php?type=get_sms&country_id=BR&operator=Total_BR&service=opt19&id={idsms}&redirectphone=0'
        response = requests.get(url, headers=headers)
        end = response.text
        codigosms = re.search(r'Your verification code is (.*?)[\s)]', end)

        if not codigosms:
            echoAndFlush("SMS não encontrado.")
            break

        echoAndFlush(f"SMS encontrado, continuando processo... Código: {codigosms.group(1)}")
        break
