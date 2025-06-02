# 📊 Visualizador de Dados CSV

Este é um projeto simples em **Python** usando **Streamlit** para visualizar arquivos CSV, exibir estatísticas básicas e gerar histogramas de colunas numéricas.

## 🚀 Como rodar o projeto

### 1️⃣ Instale as dependências

Recomendo criar um ambiente virtual (opcional):

```bash
python -m venv venv
venv\Scripts\activate   # no Windows
source venv/bin/activate  # no Linux/Mac

Instale o Streamlit e demais dependências:

    pip install streamlit pandas matplotlib

No terminal, execute:

streamlit run app.py

O navegador abrirá automaticamente em http://localhost:8501.

Exemplo de CSV para teste
Crie um arquivo chamado dados.csv com o seguinte conteúdo:

Nome,Idade,Salario
Ana,25,3000
João,30,3500
Lucas,28,4000
Maria,35,4500

✨ Funcionalidades
✅ Upload de arquivos CSV
✅ Exibição dos dados
✅ Estatísticas descritivas
✅ Geração de histogramas de colunas numéricas

visualizador_de_dados/
│
├── app.py
├── dados.csv (exemplo de teste)
└── README.md

🧑‍💻 Autor
Raphael França
GitHub: @RaphaelFranca1859