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

# --- Tabela 33 (simplificada) ---
tabela_33_metodos = ["A1","A2","B1","B2","C","D","E","F","G"]

# --- Tabelas de capacidade (exemplo simplificado; expandir com valores reais) ---
tabela_36 = {
    "Cobre": {
        2.5: {"A1": {2: 24, 3: 20}, "B1": {2: 27, 3: 23}, "C": {2: 33, 3: 28}, "D": {2: 39, 3: 34}},
    },
    "Alumínio": {
        2.5: {"A1": {2: 19, 3: 16}, "B1": {2: 21, 3: 18}, "C": {2: 26, 3: 22}, "D": {2: 31, 3: 27}},
    }
}

tabela_37 = {
    "Cobre": {
        2.5: {"A1": {2: 27, 3: 23}, "B1": {2: 30, 3: 26}, "C": {2: 36, 3: 31}, "D": {2: 42, 3: 37}},
    },
    "Alumínio": {
        2.5: {"A1": {2: 21, 3: 18}, "B1": {2: 24, 3: 20}, "C": {2: 29, 3: 25}, "D": {2: 34, 3: 29}},
    }
}

tabela_38 = {
    "Cobre": {
        2.5: {"E": {2: 28, 3: 24}, "F": {2: 30, 3: 26}, "G": {2: 32, 3: 27}},
    },
    "Alumínio": {
        2.5: {"E": {2: 22, 3: 19}, "F": {2: 24, 3: 20}, "G": {2: 25, 3: 21}},
    }
}

tabela_39 = {
    "Cobre": {
        2.5: {"E": {2: 32, 3: 28}, "F": {2: 34, 3: 30}, "G": {2: 36, 3: 31}},
    },
    "Alumínio": {
        2.5: {"E": {2: 25, 3: 21}, "F": {2: 27, 3: 23}, "G": {2: 28, 3: 24}},
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

st.header("Tabela 30 - Valores de K")
material = st.selectbox("Material:", list(valores_k.keys()))
isolacao = st.selectbox("Isolação:", ["PVC", "EPR", "XLPE"])

st.header("Tabela 33 - Métodos de Instalação")
metodo_ref = st.selectbox("Método de referência:", tabela_33_metodos)

n_condutores = st.radio("Número de condutores carregados:", [2,3,4])
corrente_projeto = st.number_input("Corrente de projeto (A):", min_value=1)

if st.button("Calcular"):
    secao = calcular_secao(material, isolacao, metodo_ref, n_condutores, corrente_projeto)
    if secao:
        st.success(f"Seção mínima: {secao} mm² ({material}, {isolacao}, método {metodo_ref}, {n_condutores} condutores)")
    else:
        st.error("Não foi encontrada seção adequada para os parâmetros informados.")
