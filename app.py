import streamlit as st

st.title("Labeling UI Prototype")
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    # Display the uploaded image directly
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
