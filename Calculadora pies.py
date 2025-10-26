import streamlit as st

st.title("📐 Square Footage Calculator")

# Initialize state
if "rooms" not in st.session_state:
    st.session_state.rooms = []
    st.session_state.total_area = 0
if "name" not in st.session_state:
    st.session_state.name = ""
if "length" not in st.session_state:
    st.session_state.length = 0.0
if "width" not in st.session_state:
    st.session_state.width = 0.0

# Function to add room
def add_room():
    name = st.session_state.name
    length = st.session_state.length
    width = st.session_state.width

    if name and length > 0 and width > 0:
        area = int(length * width)
        st.session_state.rooms.append((name, area))
        st.session_state.total_area += area

        # Clear fields
        st.session_state.name = ""
        st.session_state.length = 0.0
        st.session_state.width = 0.0

# Input fields
st.text_input("Room name", key="name")
st.number_input("Length (in feet)", min_value=0.0, format="%.2f", key="length")
st.number_input("Width (in feet)", min_value=0.0, format="%.2f", key="width")

# Button
st.button("Add room", on_click=add_room)

# Partial list
st.subheader("Partial list")
for name, area in st.session_state.rooms:
    st.write(f"{name}: {area} ft²")

# Full summary
st.subheader("Full summary (copy-friendly)")
summary = "\n".join([f"{name}: {area} ft²" for name, area in st.session_state.rooms])
summary += f"\nTotal: {st.session_state.total_area} ft²"
st.text_area("Summary", summary, height=150)
