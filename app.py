import streamlit as st

# --- dicionários Tabela 30 e Tabela 33 aqui ---

def mostrar_tabela30():
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
    categoria = st.selectbox("Categoria de instalação:", list(tabela_33_categorias.keys()))
    descricao = st.selectbox("Descrição:", list(tabela_33_categorias[categoria].keys()))
    dados33 = tabela_33_categorias[categoria][descricao]
    st.write({
        "Descrição": descricao,
        "Método de instalação": dados33['metodo'],
        "Referência": dados33['referencia']
    })
    if "imagem" in dados33:
        st.image(dados33["imagem"], caption=f"Método {dados33['metodo']}", use_column_width=True)

# --- Execução principal ---
st.title("NBR5410 - Ferramenta Interativa")

tab1, tab2 = st.tabs(["Tabela 30", "Tabela 33"])
with tab1:
    mostrar_tabela30()
with tab2:
    mostrar_tabela33()
