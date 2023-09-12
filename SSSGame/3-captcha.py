import requests
import time
import os
import base64

api_key = 'e1e76d914d7c894f0d8e18da28de642a'
api_url = "https://www.sssgame.com/api/member/getCaptcha?login&timestamp="

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

directory = os.path.join(os.getcwd(), "Imagem")
if not os.path.exists(directory):
    os.makedirs(directory)

def salvarCaptcha(api_url):
    try:
        response = requests.get(
            api_url,
            headers=headers,
            # proxies={'https': proxy_url},
            # auth=proxy_auth 
        )

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    data = response.json()

    if data['code'] == 0:
        dataImagem = data['data']['codeUrl']
        key = data['data']['key']

        codeImagem = dataImagem.split(',')[1]

        image_data = base64.b64decode(codeImagem)

        encoded_image_data = base64.b64encode(image_data)

        PastaImagem = os.path.join(directory, f"{key}.png")
        with open(PastaImagem, 'wb') as f:
            f.write(image_data)

        print(f"Chave captcha: {key}")

        return encoded_image_data
    else:
        print("Falha em pegar imagem")
    
def  resultadoCaptcha(encode):
    url = 'https://2captcha.com/in.php'

    params = {
        'key': api_key,
        'method': 'base64',
        'body': encode
    }

    response = requests.post(url, data=params)
    server_output = response.text

    _, captcha_id = server_output.split('|')

    repostaCaptcha = None
    for i in range(5):
        # time.sleep(5)

        url = f'https://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}'
        response = requests.get(url)
        server_output = response.text

        if server_output.startswith('OK'):
            repostaCaptcha = server_output[3:]
            break

    return repostaCaptcha

if __name__ == "__main__":
    encode = salvarCaptcha(api_url)
    resultado = resultadoCaptcha(encode)
    print(resultado)
