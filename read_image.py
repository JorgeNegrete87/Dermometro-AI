import streamlit as st
from PIL import Image

def read_im():
    st.title("Subir imagen PNG o JPG (máx. 100 MB)")

    uploaded_file = st.file_uploader("Selecciona una imagen PNG o JPG", type=["png", "jpg", "jpeg"], 
                                     accept_multiple_files=False)

    if uploaded_file is not None:
        # Verificamos el tamaño del archivo
        if uploaded_file.size > 100 * 1024 * 1024:  # Convertimos a bytes
            st.error("El archivo es demasiado grande. El tamaño máximo permitido es de 100 MB.")
        else:
            st.write("Imagen subida:")
            image = Image.open(uploaded_file)
            st.image(image, caption="Imagen subida", use_column_width=True)

if __name__ == "__main__":
    read_im()