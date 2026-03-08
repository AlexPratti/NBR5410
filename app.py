import streamlit as st

# Dicionário com os valores da Tabela 30 (NBR5410)
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
    },
    "Emenda soldada em cobre": {
        "PVC_<=300": {"K": 115, "Temp_inicial": 70, "Temp_final": 160},
        "PVC_>300": {"K": None, "Temp_inicial": None, "Temp_final": None},  # não definido
        "EPR_XLPE": {"K": None, "Temp_inicial": None, "Temp_final": None},  # não definido
    }
}

st.title("Tabela 30 - Valores de K (NBR5410)")

# Seleção do material
material = st.selectbox("Selecione o material do condutor:", list(valores_k.keys()))

# Seleção da isolação
isolacao = st.selectbox("Selecione o tipo de isolação:", ["PVC", "EPR/XLPE"])

# Se for PVC, perguntar a bitola
if isolacao == "PVC":
    bitola = st.radio("Selecione a seção do condutor:", ["≤ 300 mm²", "> 300 mm²"])
    chave = "PVC_<=300" if bitola == "≤ 300 mm²" else "PVC_>300"
else:
    chave = "EPR_XLPE"

# Obter valores
dados = valores_k[material][chave]

# Exibir resultado
if dados["K"] is not None:
    st.success(f"Material: {material}\nIsolação: {isolacao}\nK = {dados['K']}\n"
               f"Temperatura inicial = {dados['Temp_inicial']}°C\n"
               f"Temperatura final = {dados['Temp_final']}°C")
else:
    st.warning("Valores não normalizados para este caso.")
