from flask import Flask, render_template, request, jsonify
import pypdf
import io
import os
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key=os.environ.get("HEROKU_GEMINI_API_KEY"))

# Iniciando o modelo

model = genai.GenerativeModel('gemini-1.5-flash')


def classificar_email_e_gerar_resposta(email_content):
    
    #Função que usa a api do Gemini para classificar e gerar a resposta
    prompt_completo = f"""
    Classifique o e-mail a seguir como "Produtivo" ou "Improdutivo" e, em seguida, gere uma resposta automática curta. Considere Produtivo e-mails que precisem de uma ação a ser tomada e Improdutivo e-mails que apenas desejem felicitações, agradecimentos ou outro tipo de mensagem irrelevante para se tomar uma ação.
    Se for "Produtivo", a resposta deve ser formal e indicar que a solicitação foi recebida.
    Se for "Improdutivo", a resposta deve ser educada e apenas agradecendo a mensagem.
    E-mail: "{email_content}"
    Análise:
    """
    try:
        response = model.generate_content(prompt_completo)

        resposta_gerada = response.text.strip()

        if "Produtivo" in resposta_gerada:
            categoria = "Produtivo"
        else:
            categoria = "Improdutivo"
        
        #Extraindo a parte da resposta sugerida
        if "Resposta Automática:" in resposta_gerada:
            resposta_sugerida = resposta_gerada.split("Resposta Automática:")[1].strip()
        elif "Resposta automática:" in resposta_gerada:
            resposta_sugerida = resposta_gerada.split("Resposta automática:")[1].strip()
        else:
            resposta_sugerida = resposta_gerada
        
        return categoria, resposta_sugerida

    except Exception as error:
        print(f"Erro no processamento da IA: {error}")
        return "Erro", "Não foi possível processar o e-mail."



#Rota principal para o arquivo HTML
@app.route("/")
def index():
    return render_template("index.html")

#Rota para processar o email
@app.route("/analyze", methods=["POST"])
def analisar_email():
    
    conteudo_email = ""

    #Verifica se um texto foi colado no formulário
    if 'email-text' in request.form and request.form['email-text']:
        conteudo_email = request.form['email-text']
    #Caso contrário, verifica se foi enviado um arquivo
    elif 'email-file' in request.files and request.files['email-file'].filename:
        email_file = request.files['email-file']

        #Lê o conteúdo do arquivo.
        if email_file.filename.endswith('.txt'):
            conteudo_email = email_file.read().decode('utf-8')
        
        elif email_file.filename.endswith('.pdf'):
            try:
                #Usa a classe PdfReader para ler o pdf
                leitor_pdf = pypdf.PdfReader(io.BytesIO(email_file.read()))

                for pagina in leitor_pdf.pages:
                    conteudo_email += pagina.extract_text()
            
            except Exception as error:
                return jsonify({
                "error": f"Erro ao ler o arquivo pdf:{str(error)}"
                }), 400
    
    if not conteudo_email:
        return jsonify({
                "error": "Nenhum e-mail foi fornecido para análise."
            }), 400
    
        # Resultado de teste
    categoria, resposta_sugerida = classificar_email_e_gerar_resposta(conteudo_email)
    return jsonify({
        "categoria": categoria,
        "resposta_sugerida": resposta_sugerida
    })

if __name__ == '__main__':
    app.run(debug=True)