from flask import Flask, render_template,url_for
from os import getcwd, listdir

app = Flask(__name__) 

@app.route("/", methods=["GET"])
def home():    
    arquivos = pegar_imagens_do_tema("infantil")
    return render_template("index.html",fotos=arquivos)

if __name__ == "__main__":
    
    app.run(debug=True)


def pegar_imagens_do_tema(tema):
    # arquivos = ["Screenshot 2022-11-02 at 15-19-06 Káh Fotografia.png", 
    # "Screenshot 2022-11-02 at 15-19-28 Káh Fotografia.png",
    # "Screenshot 2022-11-02 at 15-19-50 Káh Fotografia.png",
    # "Screenshot 2022-11-02 at 15-42-28 Káh Fotografia.png",
    # "Screenshot 2022-11-02 at 15-43-45 Káh Fotografia.png",
    # ]
    arquivos = pegar_arquivos_na_pasta(tema)
    arquivos_fullpath = [f"{tema}/{arq}" for arq in arquivos]
    return arquivos_fullpath
    
def pegar_arquivos_na_pasta(tema):
    caminho_do_diretorio= f"{getcwd()}/static/{tema}"
    arquivos = [f for f in listdir(caminho_do_diretorio)]    
    return arquivos