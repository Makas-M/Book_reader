import PyPDF2
import pyttsx3

def extrair_texto_pdf(caminho_pdf):
    texto = ''
    with open(caminho_pdf, 'rb') as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
        for pagina in range(len(leitor_pdf.pages)):
            texto += leitor_pdf.pages[pagina].extract_text()
    return texto

def reproduzir_audio(texto):
    
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  # Velocidade da fala
    engine.setProperty('voice', 'pt-br') # idioma

    engine.say(texto)
    engine.runAndWait()

def main():
    caminho_pdf = 'pdf1.pdf'

    texto_do_pdf = extrair_texto_pdf(caminho_pdf)

    if texto_do_pdf:
        reproduzir_audio(texto_do_pdf)
    else:
        print("Não foi possível extrair texto do PDF.")

if __name__ == "__main__":
    main()
