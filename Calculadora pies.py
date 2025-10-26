import streamlit as st

st.title("📐 Square Footage Calculator")

# Initialize state
if "rooms" not in st.session_state:
    st.session_state.rooms = []
    st.session_state.total_area = 0
if "name" not in st.session_state:
    st.session_state.name = ""
if "length" not in st.session_state:
    st.session_state.length = ""
if "width" not in st.session_state:
    st.session_state.width = ""

# Function to add room
def add_room():
    try:
        length = float(st.session_state.length)
        width = float(st.session_state.width)
    except ValueError:
        return  # Skip if input is not valid

    name = st.session_state.name
    if name and length > 0 and width > 0:
        area = int(length * width)
        st.session_state.rooms.append((name, area))
        st.session_state.total_area += area

        # Clear fields
        st.session_state.name = ""
        st.session_state.length = ""
        st.session_state.width = ""

# Input fields (text-based for blank appearance)
st.text_input("Room name", key="name")
st.text_input("Length (in feet)", key="length")
st.text_input("Width (in feet)", key="width")

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
