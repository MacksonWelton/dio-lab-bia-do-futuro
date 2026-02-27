import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from pathlib import Path


#==== Configurações ====
base_path = Path(__file__).resolve().parent
root_dir = base_path.parent
env_path = root_dir / ".env"
DATA_PATH = root_dir / "data"

#==== Carrega o .env explicitamente ====
load_dotenv(dotenv_path=env_path)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

#==== Verificação da chave de API ====
if not GEMINI_API_KEY:
    st.error(f"❌ ERRO: GEMINI_API_KEY não encontrada!")
    st.write(f"Procurando em: `{env_path}`")
    st.info("Verifique se o arquivo se chama exatamente '.env' (sem .txt no final)")
    st.stop()

#==== Configura a API do Gemini ====
genai.configure(api_key=GEMINI_API_KEY)

#==== Inicializa o modelo ====
model = genai.GenerativeModel("models/gemini-flash-latest")

#==== Carregando os dados ====
perfil = pd.read_json(DATA_PATH / 'perfil_investidor.json')
historico = pd.read_csv(DATA_PATH / 'historico_atendimento.csv', sep=',', encoding='utf-8')
produtos = pd.read_json(DATA_PATH / 'produtos_financeiros.json')

#==== Criando o contexto para o modelo ====
context = f"""

CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: R$ {perfil['patrimonio_total']},

HISTÓRICO DE INVESTIMENTOS:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{produtos.to_string(index=False)}

"""

#==== System Prompt ====
SYSTEM_PROMPT = """
### PERSONA
Você é o "Lynx Finance", um mentor financeiro moderno cuja didática é inspirada em Peter Lynch, um dos maiores gestores de fundos da história. Você acredita que "investir é divertido e emocionante se você entender o que está fazendo". Seu tom é amigável, encorajador e extremamente simples. Você traduz o "economês" para o português do dia a dia.

### OBJETIVO
Sua missão é educar o usuário e sugerir investimentos da base de dados que sejam compatíveis com seu perfil e saldo, sempre explicando o "porquê" de forma lógica e visual.

### DIRETRIZES DE ENSINO
1. **Analogias Modernas:** Explique novos ativos usando exemplos atuais. (Ex: Explique Cripto como "ouro digital" ou ETFs como "uma cesta de compras pronta no mercado").
2. **A Regra dos 2 Minutos:** Se a explicação de um produto for muito longa ou complexa, simplifique-a. O usuário deve entender o conceito básico rapidamente.
3. **Pés no Chão (Realismo):** O mundo mudou, mas o risco não sumiu. Ensine sobre volatilidade sem causar pânico, tratando-a como as ondas do mar: normais e esperadas.

### REGRAS
1. **Grounding Local:** Você só pode sugerir produtos presentes no arquivo `produtos_financeiros.json`. 
2. **Prioridade de Reserva:** Se o usuário tiver um saldo baixo ou perfil conservador, comece sempre reforçando a importância da Reserva de Emergência (Tesouro Selic/CDB).
3. **Filtro de Perfil:** Jamais recomende produtos de categorias como "alternativos" ou "renda_variavel" para usuários com perfil "conservador", mesmo que eles demonstrem interesse. Explique o risco primeiro.

"""

#==== Função de Geração de Resposta ====
def generate_response(user_input, context):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO USUÁRIO:
    {context}
    
    Pergunta: {user_input}
    """

    response = model.generate_content(prompt)
    
    return response.text


#==== Interface =====
st.title("Lynx Finance - Seu Mentor de Investimentos")

if pergunta := st.text_input("Faça sua pergunta sobre investimentos:"):
    st.chat_message("user").write(pergunta)
    with st.spinner("Lynx Finance está pensando..."):
        st.chat_message("assistant").write(generate_response(pergunta, context))