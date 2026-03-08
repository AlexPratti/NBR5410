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

# --- Tabela 33 com imagens por método ---
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
    "Cabos em Bandeja Perfurada": {
        "Cabos unipolares": {
            "metodo": 13, "referencia": "F",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.87610e91-6071-44e1-a6d4-5ec9c9c207cc.png"
        },
    },
    "Sobre Isoladores": {
        "Condutores nus ou isolados": {
            "metodo": 18, "referencia": "G",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.8c20393d-4588-4a66-924f-f5d432aecab3.png"
        },
    },
    "Diretamente Enterrados com Proteção Mecânica Adicional": {
        "Cabos unipolares ou multipolar": {
            "metodo": 63, "referencia": "D",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.8c7b77da-d707-49c9-9fa4-b1a14083c262.png"
        },
    },
    # Aqui você pode continuar adicionando os demais métodos (21–75)
}
# --- Interface Streamlit ---
st.title("NBR5410 - Ferramenta Interativa")

# --- Seção Tabela 30 ---
st.header("Tabela 30 - Valores de K")

# Seleção do material
material = st.selectbox("Material:", list(valores_k.keys()))

# Seleção da isolação
isolacao = st.selectbox("Isolação:", ["PVC", "EPR/XLPE"])

# Seleção da bitola quando isolação for PVC
if isolacao == "PVC":
    bitola = st.radio("Seção do condutor:", ["≤ 300 mm²", "> 300 mm²"])
    chave = "PVC_<=300" if bitola == "≤ 300 mm²" else "PVC_>300"
else:
    chave = "EPR_XLPE"

# Recupera os dados da tabela
dados = valores_k[material][chave]

# Exibe resultado
st.success(
    f"K = {dados['K']}, Temp inicial = {dados['Temp_inicial']}°C, Temp final = {dados['Temp_final']}°C"
)

# --- Seção Tabela 33 ---
st.header("Tabela 33 - Métodos de Instalação")

# Primeiro o usuário escolhe a categoria
categoria = st.selectbox(
    "Selecione a categoria de instalação:",
    list(tabela_33_categorias.keys())
)

# Depois escolhe a descrição dentro da categoria
descricao = st.selectbox(
    "Selecione a descrição:",
    list(tabela_33_categorias[categoria].keys())
)

# Resultado
dados33 = tabela_33_categorias[categoria][descricao]
st.success(
    f"Descrição: {descricao}\n"
    f"Método de instalação: {dados33['metodo']}\n"
    f"Referência: {dados33['referencia']}"
)

# Exibir imagem se disponível
if "imagem" in dados33:
    st.image(
        dados33["imagem"],
        caption=f"Ilustração: Método {dados33['metodo']}",
        use_column_width=True
    )
# --- Expansão da Tabela 33 ---
tabela_33_categorias.update({
    "Eletroduto Embutido em Alvenaria": {
        "Condutores isolados ou cabos unipolares": {
            "metodo": 21, "referencia": "B1",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.eletroduto_embutido_unipolar.png"
        },
        "Cabo multipolar": {
            "metodo": 22, "referencia": "B2",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.eletroduto_embutido_multipolar.png"
        },
    },
    "Eletroduto Aparente": {
        "Condutores isolados ou cabos unipolares": {
            "metodo": 31, "referencia": "C1",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.eletroduto_aparente_unipolar.png"
        },
        "Cabo multipolar": {
            "metodo": 32, "referencia": "C2",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.eletroduto_aparente_multipolar.png"
        },
    },
    "Em Leito": {
        "Cabos unipolares": {
            "metodo": 41, "referencia": "E",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.em_leito_unipolar.png"
        },
        "Cabos multipolares": {
            "metodo": 42, "referencia": "E",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.em_leito_multipolar.png"
        },
    },
    "Canaleta Embutida em Parede": {
        "Cabos unipolares ou multipolar": {
            "metodo": 51, "referencia": "H",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.canaleta_embutida.png"
        },
    },
    "Fixado no Teto": {
        "Cabos unipolares ou multipolar": {
            "metodo": 71, "referencia": "I",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.fixado_teto.png"
        },
    },
    "Suspenso": {
        "Cabos unipolares ou multipolar": {
            "metodo": 75, "referencia": "J",
            "imagem": "https://copilot.microsoft.com/th/id/BCO.suspenso.png"
        },
    },
})
