import cv2
import os
import glob
import numpy as np
import random
from sklearn.metrics import pairwise_distances

def calcular_descritor_hog(imagem):
    win_size = (32, 32)
    block_size = (16, 16)
    block_stride = (8, 8)
    cell_size = (8, 8)
    nbins = 9

    hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)
    descritor_hog = hog.compute(imagem)
    return np.ravel(descritor_hog)

def organizar_letras(pasta_origem, pasta_destino='letras_organizadas', n_amostras=100):
    # Criar diretório para armazenar as letras organizadas
    os.makedirs(pasta_destino, exist_ok=True)

    # Pegar a lista de arquivos de letras
    arquivos_letras = glob.glob(f"{pasta_origem}/*.png")

    # Selecionar aleatoriamente amostras da lista
    amostras_selecionadas = random.sample(arquivos_letras, n_amostras)

    # Calcular e armazenar os descritores HOG das letras
    letras_descritores = {}
    for arquivo_letra in amostras_selecionadas:
        imagem_letra = cv2.imread(arquivo_letra, cv2.IMREAD_GRAYSCALE)
        descritor_hog = calcular_descritor_hog(imagem_letra)
        if descritor_hog.size > 0:  # Verificar se o descritor não está vazio
            letras_descritores[arquivo_letra] = descritor_hog

    if not letras_descritores:
        print("Descritor HOG vazio para todas as letras. Verifique as amostras.")
        return

    # Organizar as letras com base na similaridade dos descritores HOG usando distância euclidiana
    descritores_selecionados = [letras_descritores[arquivo] for arquivo in letras_descritores]
    matriz_distancias = pairwise_distances(descritores_selecionados, metric='euclidean')
    ordenacao = [amostras_selecionadas[i] for i in np.argsort(matriz_distancias.sum(axis=0))]

    # Mover as letras para a pasta de destino, organizadas pela similaridade do formato do desenho
    for i, arquivo_letra in enumerate(ordenacao):
        nome_arquivo = os.path.basename(arquivo_letra)
        novo_caminho = f"{pasta_destino}/{nome_arquivo}"
        os.replace(arquivo_letra, novo_caminho)

if __name__ == "__main__":
    organizar_letras('letras', n_amostras=100)
