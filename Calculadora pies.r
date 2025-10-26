import streamlit as st

st.title("📐 Calculadora de pies cuadrados")

# Estado
if "habitaciones" not in st.session_state:
    st.session_state.habitaciones = []
    st.session_state.total_area = 0

# Entradas
nombre = st.text_input("Nombre de la habitación")
largo = st.number_input("Largo (en pies)", min_value=0.0, format="%.2f")
ancho = st.number_input("Ancho (en pies)", min_value=0.0, format="%.2f")

if st.button("Agregar habitación"):
    if largo > 0 and ancho > 0 and nombre:
        area = int(largo * ancho)
        st.session_state.habitaciones.append((nombre, area))
        st.session_state.total_area += area

# Mostrar listado
st.subheader("Listado parcial")
for nombre, area in st.session_state.habitaciones:
    st.write(f"{nombre}: {area} sf")

# Mostrar resumen copiable
st.subheader("Resumen completo (copiable)")
resumen = "\n".join([f"{nombre}: {area} sf" for nombre, area in st.session_state.habitaciones])
resumen += f"\nTotal: {st.session_state.total_area} sf"
st.text_area("Resumen", resumen, height=150)
