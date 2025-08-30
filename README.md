# 🤖 Classificador de E-mails com IA 📧

Este projeto é uma aplicação web simples que utiliza inteligência artificial para automatizar a classificação de e-mails e gerar respostas automáticas. É uma solução para otimizar o tempo de equipes que lidam com um alto volume de correspondência diária, categorizando as mensagens como "Produtivas" ou "Improdutivas".

## ✨ Funcionalidades

* **Interface Web Responsiva:** 🌐 Desenvolvida com HTML e Bootstrap para uma experiência de usuário agradável e adaptável a diferentes telas.
* **Backend em Python:** 🐍 Utiliza o framework **Flask** para processar as requisições e a lógica da aplicação.
* **Processamento de Texto:** 📄 Capaz de ler e processar o conteúdo de e-mails inseridos diretamente ou enviados em arquivos `.txt` e `.pdf`.
* **Inteligência Artificial:** 🧠 Integração com a **API Google Gemini** para:
    * Classificação precisa de e-mails em **Produtivo** ou **Improdutivo**.
    * Geração de **respostas automáticas** sugeridas com base na classificação.

## 🚀 Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e executar a aplicação no seu computador.

### 1. Pré-requisitos

Certifique-se de que você tem o **Python 3.8+** e o **pip** instalados.

### 2. Clonar o Repositório

Abra seu terminal e clone o repositório do projeto:
```
bash
```
```
git clone https://github.com/Eduzord/classificador-email-autou.git
```
```
cd classificador-email-autou
```

### 3. Criar e Ativar o Ambiente Virtual

É uma boa prática isolar as dependências do projeto.

```
Bash
```
```
python -m venv .venv
```
##### No Windows
```
.\.venv\Scripts\activate
```
##### No macOS/Linux
```
source .venv/bin/activate
```

### 4. Instalar as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias listadas no arquivo requirements.txt:

````
pip install -r requirements.txt
````

### 5. Configurar a Chave da API

A aplicação usa a API Google Gemini. Você precisa de uma chave própria para que a IA funcione.

Acesse o [Google AI Studio](https://aistudio.google.com/app/apikey) para criar sua chave.

Na linha 9 do arquivo ```app.py``` você deve alterar para ficar dessa maneira:

```genai.configure(api_key="SUA_API_KEY_AQUI")```

 ⚠A chave só deve ser inserida se for rodar apenas localmente, nunca disponibilize o código com sua chave na internet⚠

 ### 6. Executar a Aplicação
 
Agora você pode iniciar o servidor Flask.

Inicie o arquivo ```python app.py```

Acesse http://127.0.0.1:5000 no seu navegador para ver a aplicação em funcionamento. 🎉

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python, Flask, Gunicorn
  
* **Frontend:** HTML, Bootstrap, CSS, JavaScript

* **Inteligência Artificial**: Google Gemini API

* **Processamento de Arquivos**: PyPDF
