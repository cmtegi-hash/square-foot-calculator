import streamlit as st

st.title("📐 Calculadora de pies cuadrados")

# Inicializar estado
if "habitaciones" not in st.session_state:
    st.session_state.habitaciones = []
    st.session_state.total_area = 0
if "nombre" not in st.session_state:
    st.session_state.nombre = ""
if "largo" not in st.session_state:
    st.session_state.largo = 0.0
if "ancho" not in st.session_state:
    st.session_state.ancho = 0.0

# Función para limpiar campos
def limpiar_campos():
    st.session_state.nombre = ""
    st.session_state.largo = 0.0
    st.session_state.ancho = 0.0

# Entradas con estado
st.text_input("Nombre de la habitación", key="nombre")
st.number_input("Largo (en pies)", min_value=0.0, format="%.2f", key="largo")
st.number_input("Ancho (en pies)", min_value=0.0, format="%.2f", key="ancho")

# Botón
if st.button("Agregar habitación"):
    if st.session_state.largo > 0 and st.session_state.ancho > 0 and st.session_state.nombre:
        area = int(st.session_state.largo * st.session_state.ancho)
        st.session_state.habitaciones.append((st.session_state.nombre, area))
        st.session_state.total_area += area
        limpiar_campos()

# Mostrar listado
st.subheader("Listado parcial")
for nombre, area in st.session_state.habitaciones:
    st.write(f"{nombre}: {area} sf")

# Mostrar resumen copiable
st.subheader("Resumen completo (copiable)")
resumen = "\n".join([f"{nombre}: {area} sf" for nombre, area in st.session_state.habitaciones])
resumen += f"\nTotal: {st.session_state.total_area} sf"
st.text_area("Resumen", resumen, height=150)
