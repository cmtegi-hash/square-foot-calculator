import streamlit as st

st.title("📐 Calculadora de pies cuadrados")

# Inicializar estado
if "habitaciones" not in st.session_state:
    st.session_state.habitaciones = []
    st.session_state.total_area = 0

# Función para agregar habitación
def agregar_habitacion():
    if st.session_state.nombre and st.session_state.largo > 0 and st.session_state.ancho > 0:
        area = int(st.session_state.largo * st.session_state.ancho)
        st.session_state.habitaciones.append((st.session_state.nombre, area))
        st.session_state.total_area += area

        # Limpiar campos usando widget keys
        st.session_state.nombre = ""
        st.session_state.largo = 0.0
        st.session_state.ancho = 0.0

# Entradas con claves únicas
st.text_input("Nombre de la habitación", key="nombre")
st.number_input("Largo (en pies)", min_value=0.0, format="%.2f", key="largo")
st.number_input("Ancho (en pies)", min_value=0.0, format="%.2f", key="ancho")

# Botón
st.button("Agregar habitación", on_click=agregar_habitacion)

# Mostrar listado
st.subheader("Listado parcial")
for nombre, area in st.session_state.habitaciones:
    st.write(f"{nombre}: {area} sf")

# Mostrar resumen copiable
st.subheader("Resumen completo (copiable)")
resumen = "\n".join([f"{nombre}: {area} sf" for nombre, area in st.session_state.habitaciones])
resumen += f"\nTotal: {st.session_state.total_area} sf"
st.text_area("Resumen", resumen, height=150)
