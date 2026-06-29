import streamlit as st

st.set_page_config(
    page_title="Calculadora de IMC",
    page_icon="⚖️",
    layout="centered"
)

# Estilo customizado
st.markdown("""
    <style>
    .main {
        max-width: 500px;
        margin: auto;
    }
    .stButton>button {
        width: 100%;
        height: 3.2em;
        font-size: 1.1em;
        font-weight: 600;
    }
    .big-imc {
        font-size: 4.5rem;
        font-weight: 700;
        text-align: center;
        margin: 10px 0;
    }
    .classification-box {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1 style='text-align: center; color: #1e2937;'>⚖️ Calculadora de IMC</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.1em;'>Super Detalhada</p>", unsafe_allow_html=True)
st.divider()

# Formulário
with st.form("imc_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        peso = st.text_input("Peso (kg)", placeholder="70,5", help="Ex: 70.5 ou 70,5")
    
    with col2:
        altura = st.text_input("Altura (metros)", placeholder="1,75", help="Ex: 1.75")
    
    submitted = st.form_submit_button("🧮 Calcular IMC", use_container_width=True)

if submitted:
    # Tratamento de entrada
    try:
        peso_val = float(peso.replace(",", "."))
        altura_val = float(altura.replace(",", "."))
    except:
        st.error("Por favor, digite valores numéricos válidos.")
        st.stop()

    # Validações
    if peso_val <= 0:
        st.error("O peso deve ser maior que zero.")
        st.stop()
    
    if altura_val < 0.5 or altura_val > 3.0:
        st.error("A altura deve estar entre 0.5 e 3.0 metros.")
        st.stop()

    # Cálculo
    imc = peso_val / (altura_val ** 2)

    # Resultado
    st.success("Cálculo realizado com sucesso!")

    st.markdown(f"<div class='big-imc'>{imc:.2f}</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b; margin-top:-15px;'>Seu IMC</p>", unsafe_allow_html=True)

    # Classificação
    if imc < 16.0:
        classificacao = "Magreza Grave (Grau III)"
        cor = "#1e40af"
        fundo = "#dbeafe"
        icone = "⬇️"
    elif imc < 17.0:
        classificacao = "Magreza Moderada (Grau II)"
        cor = "#1e40af"
        fundo = "#dbeafe"
        icone = "⬇️"
    elif imc < 18.5:
        classificacao = "Magreza Leve (Grau I)"
        cor = "#1e40af"
        fundo = "#dbeafe"
        icone = "⬇️"
    elif imc < 22.0:
        classificacao = "Peso Normal (Faixa de Transição Baixa)"
        cor = "#065f46"
        fundo = "#d1fae5"
        icone = "✅"
    elif imc < 25.0:
        classificacao = "Peso Normal / Ideal (Parabéns!)"
        cor = "#065f46"
        fundo = "#d1fae5"
        icone = "✅"
    elif imc < 27.5:
        classificacao = "Sobrepeso Inicial (Alerta Leve)"
        cor = "#92400e"
        fundo = "#fef3c7"
        icone = "⚠️"
    elif imc < 30.0:
        classificacao = "Sobrepeso Avançado (Pré-Obesidade)"
        cor = "#92400e"
        fundo = "#fef3c7"
        icone = "⚠️"
    elif imc < 35.0:
        classificacao = "Obesidade Grau I (Moderada)"
        cor = "#9a3412"
        fundo = "#ffedd5"
        icone = "⚠️"
    elif imc < 40.0:
        classificacao = "Obesidade Grau II (Severa)"
        cor = "#991b1b"
        fundo = "#fee2e2"
        icone = "❌"
    else:
        classificacao = "Obesidade Grau III (Mórbida)"
        cor = "#991b1b"
        fundo = "#fee2e2"
        icone = "❌"

    # Caixa de classificação
    st.markdown(f"""
        <div class="classification-box" style="background-color: {fundo}; border: 2px solid {cor}20;">
            <div style="font-size: 2rem; margin-bottom: 8px;">{icone}</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: {cor};">Classificação</div>
            <div style="font-size: 1.3rem; font-weight: 800; color: {cor};">{classificacao}</div>
        </div>
    """, unsafe_allow_html=True)

    # Aviso
    st.caption("⚠️ Lembre-se: este é apenas um indicador. Consulte um profissional de saúde.")

# Rodapé
st.divider()
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.85em;'>Feito com Python + Streamlit</p>", unsafe_allow_html=True)