# ♻️ EcoCycle

> Plataforma de descarte correto e troca/doação de itens para fomentar a economia circular.

Projeto de Extensão Universitária — Análise e Desenvolvimento de Sistemas (ADS)
Alinhado ao **ODS 12 da ONU** — Consumo e Produção Responsáveis.

---

## 🌱 Sobre o projeto

O EcoCycle é uma aplicação web que conecta pessoas que desejam descartar, trocar ou doar itens com quem pode dar uma nova utilidade a eles. O objetivo é reduzir o descarte inadequado e incentivar práticas de consumo mais conscientes e sustentáveis.

---

## 🛠️ Tecnologias

- **Python 3** + **Flask** — backend e rotas
- **Jinja2** — templates HTML
- **CSS embutido** — estilização sem dependências externas
- Armazenamento em memória (sem banco de dados externo)

---

## ⚙️ Como rodar localmente

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/ecocycle.git
cd ecocycle
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Suba o servidor**
```bash
python app.py
```


---

## ✅ Funcionalidades

- **Feed de itens** — listagem de todos os itens cadastrados com nome, categoria, estado de conservação e contato do doador
- **Filtro por categoria** — filtragem instantânea por tipo de item
- **Cadastro de itens** — formulário para publicar um novo item com validação de dados

---

## 📁 Estrutura do projeto

```
ecocycle/
├── app.py               # Rotas e lógica da aplicação
├── requirements.txt     # Dependências
└── templates/
    ├── base.html        # Layout base e estilos
    ├── index.html       # Feed e filtro
    └── cadastrar.html   # Formulário de cadastro
```

---

## 🌍 ODS 12 — Consumo e Produção Responsáveis

Este projeto contribui diretamente para a meta 12.5 da ONU, que visa reduzir substancialmente a geração de resíduos por meio da prevenção, redução, reciclagem e reutilização, promovendo a economia circular como alternativa ao descarte convencional.

---

*Desenvolvido como projeto de extensão universitária — ADS*
