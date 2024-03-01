import streamlit as st

def main():
    # Header
    st.title("Analisis Kepuasan Konsumen Franchise ABD (Ayam Bang Dava)")
    st.write("Created By Wondy Arifin")
    
    # Isi
    st.write("Di Kota Bandung, olahan daging ayam sudah tak terhitung lagi banyaknya. Setiap sudut kota, Anda begitu mudah menemui berbagai macam tempat makan yang menawarkan menu tersebut. Satu di antaranya yang patut anda sambangi adalah Kedai Ayam Bang Dava. Lokasinya berada di Jalan Mataram No 2, Cihapit, Kota Bandung.")
    
    # Gambar
    st.image("https://via.placeholder.com/300", caption="Ini adalah contoh gambar", use_column_width=True)

if __name__ == "__main__":
    main()
