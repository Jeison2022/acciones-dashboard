
import streamlit as st
import pandas as pd

# Título
st.title("📊 Dashboard de Inversiones en Acciones")

# Inicializar session_state si no existe
if "data" not in st.session_state:
    st.session_state.data = []

# Formulario de entrada
with st.form("registro_operacion"):
    st.subheader("Agregar operación")
    nombre_empresa = st.text_input("Nombre de la empresa")
    comision = st.number_input("Comisión de la comisionista (COP)", min_value=0.0, step=100.0)
    precio_compra = st.number_input("Precio de compra por acción (COP)", min_value=0.0, step=100.0)
    precio_venta = st.number_input("Precio de venta por acción (COP)", min_value=0.0, step=100.0)
    numero_acciones = st.number_input("Número de acciones", min_value=1, step=1)
    submitted = st.form_submit_button("Agregar")

    if submitted:
        ganancia_bruta = (precio_venta - precio_compra) * numero_acciones
        ganancia_neta = ganancia_bruta - comision
        porcentaje_ganancia = (ganancia_neta / (precio_compra * numero_acciones)) * 100 if precio_compra > 0 else 0

        st.session_state.data.append({
            "Empresa": nombre_empresa,
            "Comisión (COP)": comision,
            "Precio Compra (COP)": precio_compra,
            "Precio Venta (COP)": precio_venta,
            "Acciones": numero_acciones,
            "Ganancia Neta (COP)": ganancia_neta,
            "% Ganancia": porcentaje_ganancia
        })

# Mostrar tabla
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.subheader("📈 Registro de operaciones")
    st.dataframe(df.style.format({
        "Comisión (COP)": "${:,.0f}",
        "Precio Compra (COP)": "${:,.0f}",
        "Precio Venta (COP)": "${:,.0f}",
        "Ganancia Neta (COP)": "${:,.0f}",
        "% Ganancia": "{:.2f}%"
    }))
