import cv2
import os
import glob

arquivos = glob.glob('ajeitado/*')
for arquivo in arquivos:
    imagem = cv2.imread(arquivo)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

    # Em preto e branco
    _, nova_imagem = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY_INV)

    # Dividir a imagem em quatro partes iguais verticalmente
    altura, largura = imagem.shape
    largura_quarto = largura // 4

    regiao_letras = []
    for i in range(4):
        x1 = largura_quarto * i
        x2 = largura_quarto * (i + 1)
        regiao_letras.append((x1 + 3, 7, x2 - 3, 40))

    # Desenhar os contornos e separar as letras em arquivos individuais
    imagem_final = cv2.merge([imagem] * 3)
    
    i = 0
    for retangulo in regiao_letras:
        x1, y1, x2, y2 = retangulo
        imagem_letra = imagem[y1:y2, x1:x2]
        i += 1
        nome_arquivo = os.path.basename(arquivo).replace(".png", f"letra{i}.png")
        cv2.imwrite(f'letras/{nome_arquivo}', imagem_letra)
        cv2.rectangle(imagem_final, (x1, y1), (x2, y2), (0, 255, 0), 1)

    nome_arquivo = os.path.basename(arquivo)
    cv2.imwrite(f"identificado/{nome_arquivo}", imagem_final)
