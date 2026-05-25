import os
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-key")

items = [
    {
        "id": 1,
        "nome": "Notebook Dell Inspiron",
        "categoria": "Eletrônicos",
        "estado": "Bom",
        "contato": "ana@email.com",
        "descricao": "Funciona bem, bateria desgastada.",
        "data": "24/05/2025",
    },
    {
        "id": 2,
        "nome": "Sofá 3 lugares",
        "categoria": "Móveis",
        "estado": "Regular",
        "contato": "(16) 99999-1234",
        "descricao": "Alguns arranhados, estrutura intacta.",
        "data": "20/05/2025",
    },
    {
        "id": 3,
        "nome": "Caixa de livros didáticos",
        "categoria": "Livros",
        "estado": "Ótimo",
        "contato": "carlos@email.com",
        "descricao": "Ensino médio, muito bem conservados.",
        "data": "18/05/2025",
    },
]

CATEGORIAS = ["Eletrônicos", "Móveis", "Roupas", "Livros", "Eletrodomésticos", "Descarte Sustentável","Outros"]
ESTADOS = ["Ótimo", "Bom", "Regular", "Para reparo","Para Descarte"]


@app.route("/")
def index():
    categoria_filtro = request.args.get("categoria", "")
    lista = [i for i in items if categoria_filtro == "" or i["categoria"] == categoria_filtro]
    return render_template("index.html", items=lista, categorias=CATEGORIAS, filtro=categoria_filtro)


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        categoria = request.form.get("categoria", "")
        estado = request.form.get("estado", "")

        if categoria not in CATEGORIAS or estado not in ESTADOS:
            return "Dados inválidos", 400

        novo = {
            "id": len(items) + 1,
            "nome": request.form["nome"].strip()[:100],
            "categoria": categoria,
            "estado": estado,
            "contato": request.form["contato"].strip()[:100],
            "descricao": request.form.get("descricao", "").strip()[:500],
            "data": datetime.now().strftime("%d/%m/%Y"),
        }
        items.insert(0, novo)
        return redirect(url_for("index"))
    return render_template("cadastrar.html", categorias=CATEGORIAS, estados=ESTADOS)

if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug)