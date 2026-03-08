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

# --- Tabela 33 organizada por categorias (exemplo com imagens) ---
tabela_33_categorias = {
    "Eletroduto de Seção Circular Embutido em Parede Termicamente Isolante": {
        "Condutores isolados ou cabos unipolares": {
            "metodo": 1, "referencia": "A1",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.a26ec849-7b9d-4bf5-88e6-70c4155d28c2.png"
        },
        "Cabo multipolar": {
            "metodo": 2, "referencia": "A2",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.a26ec849-7b9d-4bf5-88e6-70c4155d28c2.png"
        },
    },
    "Sobre Isoladores": {
        "Condutores nus ou isolados": {
            "metodo": 18, "referencia": "G",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.8c20393d-4588-4a66-924f-f5d432aecab3.png"
        },
    },
    # ... continue adicionando imagens para os demais métodos ...
}

# --- Funções de interface ---
def mostrar_tabela30():
    st.subheader("Tabela 30 - Valores de K")
    material = st.selectbox("Material:", list(valores_k.keys()))
    isolacao = st.selectbox("Isolação:", ["PVC", "EPR/XLPE"])
    if isolacao == "PVC":
        bitola = st.radio("Seção do condutor:", ["≤ 300 mm²", "> 300 mm²"])
        chave = "PVC_<=300" if bitola == "≤ 300 mm²" else "PVC_>300"
    else:
        chave = "EPR_XLPE"
    dados = valores_k[material][chave]
    st.write({
        "K": dados['K'],
        "Temperatura inicial": f"{dados['Temp_inicial']}°C",
        "Temperatura final": f"{dados['Temp_final']}°C"
    })

def mostrar_tabela33():
    st.subheader("Tabela 33 - Métodos de Instalação")
    categoria = st.selectbox("Categoria de instalação:", list(tabela_33_categorias.keys()))
    descricao = st.selectbox("Descrição:", list(tabela_33_categorias[categoria].keys()))
    dados33 = tabela_33_categorias[categoria][descricao]

    st.write({
        "Descrição": descricao,
        "Método de instalação": dados33['metodo'],
        "Referência": dados33['referencia']
    })
    if "imagem" in dados33:
        st.image(
            dados33["imagem"],
            caption=f"Ilustração: Método {dados33['metodo']}",
            use_column_width=True
        )

# --- Execução principal com abas ---
st.title("NBR5410 - Ferramenta Interativa")

tab1, tab2 = st.tabs(["Tabela 30", "Tabela 33"])

with tab1:
    mostrar_tabela30()

with tab2:
    mostrar_tabela33()
