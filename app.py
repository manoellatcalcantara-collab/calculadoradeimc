import streamlit as st

st.title("💪 Calculadora de IMC")

st.write("Digite seus dados:")

peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
altura = st.number_input("Altura (m)", min_value=0.0, step=0.01)

if st.button("Calcular IMC"):
    if altura > 0:
        imc = peso / (altura ** 2)

        st.subheader(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            st.warning("Abaixo do peso")
        elif 18.5 <= imc < 25:
            st.success("Peso normal")
        elif 25 <= imc < 30:
            st.warning("Sobrepeso")
        else:
            st.error("Obesidade")
    else:
        st.error("Altura deve ser maior que zero")
