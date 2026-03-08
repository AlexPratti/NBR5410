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

# --- Tabela 33 (exemplo expandido; incluir todos os métodos conforme transcrição) ---
tabela_33 = {
    "Condutores isolados ou cabos unipolares em eletroduto de seção circular embutido em parede termicamente isolante": {"metodo": 1, "referencia": "A1"},
    "Cabo multipolar em eletroduto de seção circular embutido em parede termicamente isolante": {"metodo": 2, "referencia": "A2"},
    "Condutores isolados ou cabos unipolares em eletroduto aparente de seção circular sobre parede": {"metodo": 3, "referencia": "B1"},
    "Cabo multipolar em eletroduto aparente de seção circular sobre parede": {"metodo": 4, "referencia": "B1"},
    "Condutores isolados ou cabos unipolares em eletroduto aparente de seção não-circular sobre parede": {"metodo": 5, "referencia": "B1"},
    "Cabo multipolar em eletroduto aparente de seção não-circular sobre parede": {"metodo": 6, "referencia": "B1"},
    "Condutores isolados ou cabos unipolares em eletroduto de seção circular embutido em alvenaria": {"metodo": 7, "referencia": "B2"},
    "Cabo multipolar em eletroduto de seção circular embutido em alvenaria": {"metodo": 8, "referencia": "B2"},
    "Cabos unipolares ou cabo multipolar sobre parede ou espaçado desta menos de 0,3 vez o diâmetro do cabo": {"metodo": 11, "referencia": "C"},
    "Cabos unipolares ou cabo multipolar fixado diretamente no teto": {"metodo": 11, "referencia": "C"},
    "Cabos unipolares ou cabo multipolar afastado do teto mais de 0,3 vez o diâmetro do cabo": {"metodo": 11, "referencia": "C"},
    "Cabos unipolares ou cabo multipolar em bandeja não-perfurada, perfurada ou prateleira": {"metodo": 12, "referencia": "E (multipolar)"},
    "Cabos unipolares em bandeja perfurada": {"metodo": 13, "referencia": "F (unipolares)"},
    "Condutores nus ou isolados sobre isoladores": {"metodo": 18, "referencia": "G"},
    "Cabos diretamente enterrados com proteção mecânica adicional": {"metodo": 63, "referencia": "D"},
    "Cabo multipolar embutido diretamente em parede termicamente isolante": {"metodo": 51, "referencia": "A1"},
    "Cabos unipolares ou cabo multipolar embutido(s) diretamente em alvenaria sem proteção mecânica adicional": {"metodo": 52, "referencia": "C"},
    "Cabos unipolares ou cabo multipolar embutido(s) diretamente em alvenaria com proteção mecânica adicional": {"metodo": 53, "referencia": "C"},
    "Cabo multipolar em eletroduto ou canaleta não-ventilada enterrado": {"metodo": 61, "referencia": "D"},
    "Cabos unipolares em eletroduto ou canaleta não-ventilada enterrado": {"metodo": 61, "referencia": "D"},
    "Cabos unipolares ou cabo multipolar diretamente enterrado(s), com proteção mecânica adicional": {"metodo": 63, "referencia": "D"},
    "Condutores isolados ou cabos unipolares em moldura": {"metodo": 71, "referencia": "A1"},
    "Condutores isolados ou cabos unipolares em canaleta provida de separações sobre parede": {"metodo": 72, "referencia": "B1"},
    "Cabo multipolar em canaleta provida de separações sobre parede": {"metodo": 72, "referencia": "B2"},
    "Condutores isolados em eletroduto, cabos unipolares ou cabo multipolar embutido(s) em caixilho de janela": {"metodo": 74, "referencia": "A1"},
    "Condutores isolados ou cabos unipolares em canaleta embutida em parede": {"metodo": 75, "referencia": "B1"},
    "Cabo multipolar em canaleta embutida em parede": {"metodo": 75, "referencia": "B2"},
    # ... incluir todos os métodos até o 75A conforme transcrição completa
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
descricao = st.selectbox("Selecione a descrição:", list(tabela_33.keys()))
dados33 = tabela_33[descricao]
st.success(f"Método de instalação: {dados33['metodo']}, Referência: {dados33['referencia']}")
