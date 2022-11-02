from flask import Flask, render_template,url_for, escape
from os import getcwd, listdir

app = Flask(__name__) 


temas = {
    "empoderamento": "Empoderamento",
    "infantil": "Infantil",
    "eventos": "Eventos",
}

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():    
    arquivos = pegar_imagens_do_tema("infantil")
    return render_template("index.html",fotos=arquivos)

@app.route("/tema/<tema_arg>", methods=["GET"])
def tema(tema_arg=None):    
    tema = escape(tema_arg)
    arquivos = pegar_imagens_do_tema(tema)
    pagina = f"tema.html"
    tema_display_name = pegar_nome_para_display(tema)
    return render_template(pagina,fotos=arquivos, tema_display=tema_display_name)


def pegar_imagens_do_tema(tema):
    arquivos = pegar_arquivos_na_pasta(tema)
    arquivos_fullpath = [f"{tema}/{arq}" for arq in arquivos]
    return arquivos_fullpath

def pegar_arquivos_na_pasta(tema):
    caminho_do_diretorio= f"{getcwd()}/static/{tema}"
    arquivos = [f for f in listdir(caminho_do_diretorio)]    
    return arquivos

def pegar_nome_para_display(tema):
    return temas[tema]
    
if __name__ == "__main__":
    app.run(debug=True)
