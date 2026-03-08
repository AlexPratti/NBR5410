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

# --- Tabela 33 (exemplo parcial, deve ser expandida com todos os métodos) ---
tabela_33 = {
    "Condutores isolados ou cabos unipolares em eletroduto de seção circular embutido em parede termicamente isolante": {"metodo": 1, "referencia": "A1"},
    "Cabo multipolar em eletroduto de seção circular embutido em parede termicamente isolante": {"metodo": 2, "referencia": "A2"},
    "Cabos unipolares ou cabo multipolar sobre parede ou espaçado desta menos de 0,3 vez o diâmetro do cabo": {"metodo": 11, "referencia": "C"},
    "Cabos unipolares ou cabo multipolar em bandeja perfurada": {"metodo": 13, "referencia": "F (unipolares)"},
    "Condutores nus ou isolados sobre isoladores": {"metodo": 18, "referencia": "G"},
    "Cabos diretamente enterrados com proteção mecânica adicional": {"metodo": 63, "referencia": "D"},
    "Cabo multipolar embutido diretamente em parede termicamente isolante": {"metodo": 51, "referencia": "A1"},
    # ... incluir todos os métodos até o 75A
}

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
