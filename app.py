import pandas as pd
import streamlit as st
from streamlit import session_state as session
from PIL import Image
import os
from recommend import recommend_table
from text import show_text_elements
import time

@st.cache_data(persist=True, show_spinner=False)
def load_data():
    
    df = pd.read_csv("skincare-fixed.csv")
    return df

def load_image(img):
	im = Image.open(os.path.join(img))
	return im

image = Image.open('img/image.png')

st.set_page_config(page_title='Skincare-Rec.',page_icon=image,layout="wide")

col1, col2 = st.columns([1, 8]) 

with col1: 
    st.image(image, width=100)


with col2:  
    st.title("""
    SISTEM REKOMENDASI SKINCARE
    """)

st.text("")
st.text("")

tab1, tab2, tab3 = st.tabs(["Rekomendasi","Skin Type Guide","Skincare Routine"])
	
with tab1:

    df = load_data()
    
    st.subheader("""
    Rekomendasi SKINCARE
    Temukan skincare yang cocok untukmu ✨
    """)

    st.text("")
    st.text("")
    st.text("")
    st.text("")

    desc = st.text_input(label="Deskripsikan jenis kulit dan keluhan atau tujuan memakai skincare", max_chars=50, help="contoh: kulit kering berjerawat noda hitam", label_visibility="visible")
    for i in desc.split():
        if i == 'jerawat':
            st.warning("Jangan gunakan PEELING jika Anda sedang berjerawat")

    st.text("")
    st.text("")

    allergen = st.radio(
    "Apakah memiliki alergi?",
    ('Ya', 'Tidak'))

    st.text("")
    st.text("")

    buffer1, col1, buffer2 = st.columns([2, 1.35, 1])

    is_clicked = col1.button(label="Rekomendasi")

    st.text("")
    st.text("")
    st.text("")

    if is_clicked:
        start = time.time()

        recommended_skincare = recommend_table(desc, allergen)
        def path_to_image_html(path):
            return '<img src="' + path + '" width="130" >'

        recommended_skincare['DESKRIPSI'] = recommended_skincare['DESKRIPSI'].str.replace('\n', '<br>')

        def add_row_color(row):
            if row.name < 3:  # Hanya warnai 3 baris pertama
                return ['background-color: lightyellow'] * len(row)
            return [''] * len(row)

        if recommended_skincare.empty:
            st.error("No recommendations found for the given description.")
        else:
            st.title("Here's your recommendations")
            st.success("Success in {} seconds, giving {} products".format(time.time() - start, recommended_skincare.shape[0]))
            
            styled_table = recommended_skincare.reset_index(drop=True).style \
                .apply(add_row_color, axis=1) \
                .format(dict(GAMBAR=path_to_image_html))

            styled_table = styled_table.set_properties(subset=['DESKRIPSI'], **{'font-size': '12px'})
            
            table_html = styled_table.hide(axis='index').to_html()
            
            responsive_table_css = """
                <style>
                    .responsive-table {
                        overflow-x: auto;
                    }
                </style>
            """

            responsive_table_html = responsive_table_css + table_html

            st.markdown(f'<div class="responsive-table">{responsive_table_html}</div>', unsafe_allow_html=True)

    st.text("")
    
with tab2:
    st.subheader("""
        SKIN TYPE GUIDE
        Kenali jenis kulitmu!
        """
        )

    st.markdown("""
        <style>
            .responsive {
                width: 100%;
                max-width: 400px;
                height: auto;
            }
        </style>
    """, unsafe_allow_html=True)

    st.image(load_image('img/jenis_kulit.jpg'))


    result = show_text_elements()

    st.text(result)
        
with tab3:
    st.subheader("""
    SKINCARE ROUTINE
    Rangkaian perawatan skincare untuk pagi :mostly_sunny: dan malam :crescent_moon:
    """)
    st.text("")
    st.text("")
    st.image(load_image('img/sc-routine.jpg'), use_column_width=True)