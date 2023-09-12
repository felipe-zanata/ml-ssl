from tratar_captcha import tratar_imagens
from keras.models import load_model
from helpers import resize_to_fit
from imutils import paths
import numpy as np
import pickle
import cv2
import os

def quebrar_captcha():
    with open("rotulos_modelo.dat", "rb") as arquivo_tradutor:
        lb = pickle.load(arquivo_tradutor)
    
    modelo = load_model("modelo_treinado.hdf5")

    tratar_imagens("resolver", pasta_destino="resolver")

    captchas = []
    arquivos = list(paths.list_images("resolver"))
    for arquivo in arquivos:
        imagem = cv2.imread(arquivo)
        imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
        # em preto e branco
        _, nova_imagem = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY_INV)

        # Dividir a imagem em quatro partes iguais verticalmente
        altura, largura = imagem.shape
        largura_quarto = largura // 4

        regiao_letras = []
        for i in range(4):
            x1 = largura_quarto * i
            x2 = largura_quarto * (i + 1)
            regiao_letras.append((x1 + 3, 7, x2 - 3, 40))
        
        regiao_letras = sorted(regiao_letras, key=lambda x: x[0])

        # desenhar os contornos e separar as letras em arquivos individuais

        imagem_final = cv2.merge([imagem] * 3)

        i = 0
        for retangulo in regiao_letras:
            x1, y1, x2, y2 = retangulo
            imagem_letra = imagem[y1:y2, x1:x2]
            i += 1
            nome_arquivo = os.path.basename(arquivo).replace(".png", f"letra{i}.png")
            # cv2.imwrite(f'letras/{nome_arquivo}', imagem_letra)
            cv2.rectangle(imagem_final, (x1, y1), (x2, y2), (0, 255, 0), 1)

        nome_arquivo = os.path.basename(arquivo)
        cv2.imwrite(f"resolver/{nome_arquivo}", imagem_final)

        previsao = []

        i = 0
        for retangulo in regiao_letras:
            x, y, largura, altura = retangulo
            imagem_letra = imagem[y-2:y+altura+2, x-2:x+largura+2]
            imagem_letra = resize_to_fit(imagem_letra, 20, 20)

            imagem_letra = np.expand_dims(imagem_letra, axis=2)
            imagem_letra = np.expand_dims(imagem_letra, axis=0)

            letra_prevista = modelo.predict(imagem_letra)
            letra_prevista = lb.inverse_transform(letra_prevista)[0]
            previsao.append(letra_prevista)
        
        texto_previsao = "".join(previsao)
        print(texto_previsao)
        captchas.append(texto_previsao)

    print(captchas)
        # return texto_previsao

if __name__ == "__main__":
    quebrar_captcha()