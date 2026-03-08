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
    # ... (demais categorias iguais ao seu código original) ...
}

# --- Tabelas 36 a 39 (estrutura completa; preencher com valores reais da norma) ---
tabela_36 = {
    "Cobre": {
        # exemplo: seção nominal: {metodo: {n_condutores: capacidade}}
        1.5: {"A1": {2: 18, 3: 15}, "A2": {2: 20, 3: 17}, "B1": {2: 21, 3: 18}, "B2": {2: 23, 3: 20}, "C": {2: 25, 3: 21}, "D": {2: 30, 3: 26}},
        # ... preencher todas as seções conforme tabela 36 ...
    },
    "Alumínio": {
        # ... preencher conforme tabela 36 ...
    }
}

tabela_37 = {
    "Cobre": {
        # ... preencher conforme tabela 37 ...
    },
    "Alumínio": {
        # ... preencher conforme tabela 37 ...
    }
}

tabela_38 = {
    "Cobre": {
        # ... preencher conforme tabela 38 (PVC, métodos E/F/G) ...
    },
    "Alumínio": {
        # ... preencher conforme tabela 38 ...
    }
}

tabela_39 = {
    "Cobre": {
        # ... preencher conforme tabela 39 (EPR/XLPE, métodos E/F/G) ...
    },
    "Alumínio": {
        # ... preencher conforme tabela 39 ...
    }
}

# --- Função de cálculo ---
def calcular_secao(material, isolacao, metodo_ref, n_condutores, corrente_projeto):
    if isolacao == "PVC":
        if metodo_ref in ["E","F","G"]:
            tabela = tabela_38[material]
        else:
            tabela = tabela_36[material]
    else:  # EPR ou XLPE
        if metodo_ref in ["E","F","G"]:
            tabela = tabela_39[material]
        else:
            tabela = tabela_37[material]

    for secao, valores in tabela.items():
        if metodo_ref in valores and n_condutores in valores[metodo_ref]:
            capacidade = valores[metodo_ref][n_condutores]
            if capacidade >= corrente_projeto:
                return secao
    return None

# --- Interface Streamlit ---
st.title("NBR5410 - Ferramenta Interativa")

# --- Seção Tabela 30 ---
st.header("Tabela 30 - Valores de K")
material = st.selectbox("Material:", list(valores_k.keys()))
isolacao = st.selectbox("Isolação:", ["PVC", "EPR", "XLPE"])
if isolacao == "PVC":
    bitola = st.radio("Seção do condutor:", ["≤ 300 mm²", "> 300 mm²"])
    chave = "PVC_<=300" if bitola == "≤ 300 mm²" else "PVC_>300"
else:
    chave = "EPR_XLPE"
dados = valores_k[material][chave]
st.success(f"K = {dados['K']}, Temp inicial = {dados['Temp_inicial']}°C, Temp final = {dados['Temp_final']}°C")

# --- Seção Tabela 33 ---
st.header("Tabela 33 - Métodos de Instalação")
categoria = st.selectbox("Selecione a categoria de instalação:", list(tabela_33_categorias.keys()))
descricao = st.selectbox("Selecione a descrição:", list(tabela_33_categorias[categoria].keys()))
dados33 = tabela_33_categorias[categoria][descricao]
st.success(f"Descrição: {descricao}\nMétodo de instalação: {dados33['metodo']}\nMétodo de referência: {dados33['referencia']}")

# --- Complemento: cálculo da seção ---
st.header("Dimensionamento do Condutor")
n_condutores = st.radio("Número de condutores carregados:", [2,3,4])
corrente_projeto = st.number_input("Corrente de projeto (A):", min_value=1)

if st.button("Calcular seção mínima"):
    secao = calcular_secao(material, isolacao, dados33['referencia'], n_condutores, corrente_projeto)
    if secao:
        st.success(f"Seção mínima: {secao} mm² ({material}, {isolacao}, método {dados33['referencia']}, {n_condutores} condutores)")
    else:
        st.error("Não foi encontrada seção adequada para os parâmetros informados.")
