import streamlit as st

def show_text_elements():  

    st.write("")

    st.write("Terdapat lima jenis kulit manusia, yakni normal, kering, berminyak, kombinasi, dan kulit sensitif.")

    st.write("Sebelum memilih produk skincare sangat penting untuk mengenal jenis kulit kita.")

    st.markdown("""
        1. **:red[Jenis kulit normal]**, biasanya tidak memiliki masalah pada kulit.
            Pori-pori tidak terlalu besar, kulit tidak kering dan tidak berminyak.
        """)

    st.markdown("""
        2. **:red[Jenis kulit berminyak]**, 
        pada jenis kulit berminyak ditandai dengan pori-pori besar, terdapat sedikit jerawat, dan terdapat komedo.
        """)
    
    st.markdown("""
        3. **:red[Jenis kulit kombinasi]**, 
        pada jenis kulit kombinasi ini ialah kombinasi antara kulit yang normal dan berminyak. 
        Biasanya didaerah T-zone pori-pori terlihat lebih besar, terdapat komedo dan jerawat. 
        Sedangkan didaerah pipi pori-pori tidak terlalu besar dan tampak normal, kondisi kulit pun tidak terlalu kering dan tidak terlalu berminyak.
        """)
    
    st.markdown("""
        4. **:red[Jenis kulit berminyak]**, 
        pada jenis ini biasanya ditandai dengan kulit bersisik, pori-pori tidak terlihat, tidak ada minyak yang keluar, dan terdapat garis-garis halus karena kondisi kulit terlalu kering. 
        Jenis kulit kering ini akan mudah mengalami iritasi dan mudah lecet.
        """)
    
    st.markdown("""
       5. **:red[Jenis kulit sensitif]**, 
        seseorang yang memiliki jenis kulit sensitif harus berhati-hati menggunakan produk. Memiliki jenis kulit sensitif sangat disarankan untuk berkonsultasi dengan dokter, karena tipe kulit sensitif memiliki beberapa tipe yaitu:
        
            a. **:blue[Tipe sensitif berjerawat]**, 
                yang dimaksud dalam tipe kulit sensitif ini apabila menggunakan jenis kosmetik tertentu akan timbul jerawat atau breakout dan akan timbul warna kemerahan pada wajah.
            
            b. **:blue[Tipe kemerahan]** yang berupa kulit wajah akan terasa panas dan memerah.

            c. **:blue[Tipe tertusuk]**, 
                pada tipe ini ketika menggunakan kosmetik kulit wajah tidak memerah, namun kulit terasa seperti tertusuk.

            d. **:blue[Tipe kering]**, 
                jenis kulit sensitif kering ini akan mudah mengalami lecet dan lebih kering dari tipe kulit kering. Tampilan dari tipe kulit sensitif kering ini terlihat lebih banyak sisiknya. Kulit akan mudah lecet, iritasi, dan mudah gatal.""")
    
    return