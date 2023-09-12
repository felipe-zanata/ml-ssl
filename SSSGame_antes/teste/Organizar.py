import cv2
import os
import glob
import numpy as np
from sklearn.cluster import KMeans
import random

def organizar_letras(pasta_origem, pasta_destino='letras_organizadas', n_amostras=1000):
    # Criar diretório para armazenar as letras organizadas
    os.makedirs(pasta_destino, exist_ok=True)

    # Pegar a lista de arquivos de letras
    arquivos_letras = glob.glob(f"{pasta_origem}/*.png")

    # Selecionar aleatoriamente mil amostras da lista
    amostras_selecionadas = random.sample(arquivos_letras, n_amostras)

    # Ordenar as letras pela proximidade de aparência usando o K-Means com um único cluster
    letras = []
    for arquivo_letra in amostras_selecionadas:
        imagem_letra = cv2.imread(arquivo_letra, cv2.IMREAD_GRAYSCALE)
        letra = imagem_letra.flatten()
        letras.append(letra)

    X = np.array(letras)
    n_letras = len(letras)
    kmeans = KMeans(n_clusters=n_letras, random_state=0)
    kmeans.fit(X)

    # Ordenar os índices das letras com base na ordem do K-Means
    ordenacao = np.argsort(kmeans.labels_)

    # Mover as letras para a pasta de destino, organizadas pela proximidade de aparência
    for i, idx in enumerate(ordenacao):
        arquivo_letra = amostras_selecionadas[idx]

        nome_arquivo = os.path.basename(arquivo_letra)
        novo_caminho = f"{pasta_destino}/{nome_arquivo}"
        os.replace(arquivo_letra, novo_caminho)

if __name__ == "__main__":
    organizar_letras('letras', n_amostras=100)
