import base64
import glob

arquivos = glob.glob("Imagem/*")
for arquivo in arquivos:
    encode_image = base64.b64encode(arquivo)
    print(encode_image)



