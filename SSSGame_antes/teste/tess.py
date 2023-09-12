import cv2
import pytesseract

def preprocess_image(image_path):
    # Leitura da imagem em escala de cinza
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Aplicar binarização com limiar adaptativo
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    # Aplicar fechamento (closing)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
    # Remoção de ruído usando filtro de mediana
    img = cv2.medianBlur(img, 3)
    
    return img

if __name__ == "__main__":
    image_path = "Imagem1.png"
    
    # Pré-processar a imagem
    preprocessed_image = preprocess_image(image_path)
    
    # Salvar a imagem pré-processada (opcional, apenas para visualização)
    cv2.imwrite("preprocessed_image.png", preprocessed_image)
    
    # Reconhecimento óptico de caracteres (OCR) com o Tesseract na imagem pré-processada
    texto_detectado = pytesseract.image_to_string(preprocessed_image)
    
    if texto_detectado.strip():  # Verifica se há algum texto reconhecido
        print("Texto na imagem:")
        print(texto_detectado)
    else:
        print("Nenhum texto foi detectado na imagem.")
