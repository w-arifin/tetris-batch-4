import streamlit as st

def main():
    # Header
    st.title("Analisis Kepuasan Konsumen Franchise ABD (Ayam Bang Dava)")
    st.write("Created by Wondy Arifin")
    
    # Isi
    st.write("ABD merupakan kepanjangan dari Ayam Bang Dava merupakan restoran yang terkenal dengan penjualannya yaitu Ayam Geprek.")
    
    # Gambar
    st.image("https://via.placeholder.com/300", caption="Ini adalah contoh gambar", use_column_width=True)

if __name__ == "__main__":
    main()
