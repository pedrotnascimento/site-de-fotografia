from flask import Flask, render_template,url_for, escape
from os import getcwd, listdir
from copy import copy

app = Flask(__name__) 


temas = {
    "empoderamento": {
        "nome":"Empoderamento", 
        "descricao": """
        Atitude. Carisma. Vontade de viver. 
        Capture esse momento do tempo. 
        Mostre a sua energia para o mundo e prove para o que veio"""},
    "infantil": {"nome":"Infantil",
    "descricao": """Anjinho que está crescendo ou anjinho que vai nascer.
    Seu amor vai ser o mesmo para sempre. 
    Que tal guardar uma recordação?"""},
    "eventos": {"nome":"Eventos",
    "descricao": """Momentos felizes custam pra acontecer e acabam. 
    Mas a memória nunca vai esquecer o que é guardado para sempre nos corações.
    Fotografamos esse momento único, seu sentimento sempre poderá ser resgatado"""}
}

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():    
    temas_copy = copy(temas)
    temas_list = []
    for tema in temas_copy:
        arq = pegar_imagens_do_tema(tema)
        temas_copy[tema]["foto"] = arq[0]
        temas_copy[tema]["tema_id"] = tema
        temas_list.append(temas_copy[tema])
    
    return render_template("index.html",temas=temas_list)

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
    return temas[tema]["nome"]
    
if __name__ == "__main__":
    app.run(debug=True)
