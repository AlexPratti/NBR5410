import streamlit as st

# --- Tabela 30 ---
valores_k = {
    "Cobre": {
        "PVC_<=300": {"K": 115, "Temp_inicial": 70, "Temp_final": 160},
        "PVC_>300": {"K": 103, "Temp_inicial": 70, "Temp_final": 140},
        "EPR_XLPE": {"K": 143, "Temp_inicial": 90, "Temp_final": 250},
    },
    "Alumínio": {
        "PVC_<=300": {"K": 76, "Temp_inicial": 70, "Temp_final": 160},
        "PVC_>300": {"K": 68, "Temp_inicial": 70, "Temp_final": 140},
        "EPR_XLPE": {"K": 94, "Temp_inicial": 90, "Temp_final": 250},
    }
}

# --- Tabela 33 organizada por categorias ---
tabela_33_categorias = {
    "Eletroduto de Seção Circular Embutido em Parede Termicamente Isolante": {
        "Condutores isolados ou cabos unipolares": {"metodo": 1, "referencia": "A1"},
        "Cabo multipolar": {"metodo": 2, "referencia": "A2"},
    },
    "Eletroduto Aparente de Seção Circular Sobre Parede ou Espaçado desta Menos de 0,3 vezes o Diâmetro do Eletroduto": {
        "Condutores isolados ou cabos unipolares": {"metodo": 3, "referencia": "B1"},
        "Cabo multipolar": {"metodo": 4, "referencia": "B1"},
    },
    "Eletroduto Aparente de Seção Não Circular Sobre Parede": {
        "Condutores isolados ou cabos unipolares": {"metodo": 5, "referencia": "B1"},
        "Cabo multipolar": {"metodo": 6, "referencia": "B1"},
    },
    "Eletroduto de Seção Circular Embutido em Alvenaria": {
        "Condutores isolados ou cabos unipolares": {"metodo": 7, "referencia": "B2"},
        "Cabo multipolar": {"metodo": 8, "referencia": "B2"},
    },
    "Sobre Parede ou Espaçado desta Menos de 0,3 vezes o Diâmetro do Cabo": {
        "Cabos unipolares ou multipolar": {"metodo": 11, "referencia": "C"},
    },
    "Fixado Diretamente no Teto": {
        "Cabos unipolares ou multipolar": {"metodo": 11, "referencia": "C"},
    },
    "Afastado do Teto mais de 0,3 vezes o Diâmetro do Cabo": {
        "Cabos unipolares ou multipolar": {"metodo": 11, "referencia": "C"},
    },
    "Bandeja Não-Perfurada, Perfilado ou Prateleira": {
        "Cabos unipolares ou multipolar": {"metodo": 12, "referencia": "E/F"},
    },
    "Bandeja Não-Perfurada Horizontal ou Vertical": {
        "Cabos unipolares": {"metodo": 13, "referencia": "F"},
    },
    "Suportes Horizontais, Eletrocalha Aramada ou Tela": {
        "Cabos unipolares ou multipolar": {"metodo": 14, "referencia": "E/F"},
    },
    "Afastado(s) da Parede mais de 0,3 vezes o Diâmetro do Cabo": {
        "Cabos unipolares ou multipolar": {"metodo": 15, "referencia": "E/F"},
    },
    "Em Leito": {
        "Cabos unipolares ou multipolar": {"metodo": 16, "referencia": "E/F"},
    },
    "Suspenso(s) por Cabo de Suporte, Incorporado ou Não": {
        "Cabos unipolares ou multipolar": {"metodo": 17, "referencia": "E/F"},
    },
    "Sobre Isoladores": {
        "Condutores nus ou isolados": {"metodo": 18, "referencia": "G"},
    },
    "Em Espaço de Construção": {
        "Cabos unipolares ou multipolar": {"metodo": 21, "referencia": "B1/B2"},
    },
    "Eletroduto de Seção Circular em Espaço de Construção": {
        "Condutores isolados": {"metodo": 22, "referencia": "B1/B2"},
        "Cabos unipolares ou multipolar": {"metodo": 23, "referencia": "B2"},
    },
    "Eletroduto de Seção Não-Circular ou Eletrocalha em Espaço de Construção": {
        "Condutores isolados": {"metodo": 24, "referencia": "B1/B2"},
        "Cabos unipolares ou multipolar": {"metodo": 25, "referencia": "B2"},
    },
    "Eletroduto de Seção Não-Circular Embutido em Alvenaria": {
        "Condutores isolados": {"metodo": 26, "referencia": "B2/D1"},
        "Cabos unipolares ou multipolar": {"metodo": 27, "referencia": "B2"},
    },
    "Eletrocalha Sobre Parede em Percurso Horizontal ou Vertical": {
        "Condutores isolados ou cabos unipolares": {"metodo": 31, "referencia": "B1"},
        "Cabo multipolar": {"metodo": 31, "referencia": "B2"},
    },
    "Canaleta Fechada Embutida no Piso": {
        "Condutores isolados ou cabos unipolares": {"metodo": 33, "referencia": "B1"},
        "Cabo multipolar": {"metodo": 34, "referencia": "B2"},
    },
    "Eletrocalha ou Perfilado Suspensa(o)": {
        "Cabo multipolar": {"metodo": 36, "referencia": "B2"},
    },
    "Eletroduto de Seção Circular Contido em Canaleta Fechada em Percurso Horizontal ou Vertical": {
        "Condutores isolados ou cabos unipolares": {"metodo": 41, "referencia": "B1/B2"},
    },
    "Eletroduto de Seção Circular Contido em Canaleta Ventilada Embutida no Piso": {
        "Condutores isolados": {"metodo": 42, "referencia": "B1"},
        "Cabos unipolares ou multipolar": {"metodo": 43, "referencia": "B1"},
    },
    "Embutido Diretamente em Parede Termicamente Isolante": {
        "Cabo multipolar": {"metodo": 51, "referencia": "A1"},
    },
    "Embutido(s) Diretamente em Alvenaria sem Proteção Mecânica Adicional": {
        "Cabos unipolares ou multipolar": {"metodo": 52, "referencia": "C"},
    },
    "Embutido(s) Diretamente em Alvenaria com Proteção Mecânica Adicional": {
        "Cabos unipolares ou multipolar": {"metodo": 53, "referencia": "C"},
    },
    "Eletroduto (de Seção Circular ou Não) ou em Canaleta não Ventilada Enterrada(o)": {
        "Cabo multipolar": {"metodo": 61, "referencia": "D"},
        "Cabos unipolares": {"metodo": 61, "referencia": "D"},
    },
    "Diretamente Enterrados com Proteção Mecânica Adicional": {
        "Cabos unipolares ou multipolar": {"metodo": 63, "referencia": "D"},
    },
    "Em Moldura": {
        "Condutores isolados ou cabos unipolares": {"metodo": 71, "referencia": "A1"},
    },
    "Canaleta Provida de Separações Sobre Parede": {
        "Condutores isolados ou cabos unipolares": {"metodo": 72, "referencia": "B1"},
        "Cabo multipolar": {"metodo": 72, "referencia": "B2"},
    },
    "Embutido(s) em Caixilho de Porta": {
        "Condutores isolados ou cabos Embutido(s) em Caixilho de Porta": {
        "Condutores isolados ou cabos unipolares": {"metodo": 74, "referencia": "A1"},
    },
    "Embutido(s) em Caixilho de Janela": {
        "Condutores isolados ou cabos unipolares": {"metodo": 74, "referencia": "A1"},
    },
    "Canaleta Embutida em Parede": {
        "Condutores isolados ou cabos unipolares": {"metodo": 75, "referencia": "B1"},
        "Cabo multipolar": {"metodo": 75, "referencia": "B2"},
    },
}

# --- Interface Streamlit ---
st.title("NBR5410 - Ferramenta Interativa")

# --- Seção Tabela 30 ---
st.header("Tabela 30 - Valores de K")
material = st.selectbox("Material:", list(valores_k.keys()))
isolacao = st.selectbox("Isolação:", ["PVC", "EPR/XLPE"])
if isolacao == "PVC":
    bitola = st.radio("Seção do condutor:", ["≤ 300 mm²", "> 300 mm²"])
    chave = "PVC_<=300" if bitola == "≤ 300 mm²" else "PVC_>300"
else:
    chave = "EPR_XLPE"
dados = valores_k[material][chave]
st.success(f"K = {dados['K']}, Temp inicial = {dados['Temp_inicial']}°C, Temp final = {dados['Temp_final']}°C")

# --- Seção Tabela 33 ---
st.header("Tabela 33 - Métodos de Instalação")

# Primeiro o usuário escolhe a categoria
categoria = st.selectbox("Selecione a categoria de instalação:", list(tabela_33_categorias.keys()))

# Depois escolhe a descrição dentro da categoria
descricao = st.selectbox("Selecione a descrição:", list(tabela_33_categorias[categoria].keys()))

# Resultado
dados33 = tabela_33_categorias[categoria][descricao]
st.success(f"Descrição: {descricao}\nMétodo de instalação: {dados33['metodo']}\nMétodo de referência: {dados33['referencia']}")
