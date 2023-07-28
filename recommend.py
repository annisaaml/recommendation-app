import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Record start time
import time
start = time.time()

df = pd.read_csv("skincare-fixed.csv")

skin_type = df['skin_type'].unique()
keywords_list = df['keywords'].unique()

def recommend_table(description, allergen=None):

    data = df.copy()

    # Extract skin type
    st_input = []
    for st in skin_type:
        if st in description:
            st_input.append(st)
            description = description.replace(st, "")

    res_st = ''.join(st_input)

    for i in description.split():
        if i == 'berjerawat':
            data = data[data['KATEGORI'] != 'peeling']
            
    # Extract keyword
    keyword_input = []
    for keyword in keywords_list:
        if keyword in description:
            keyword_input.append(keyword)
            description = description.replace(keyword, "")

    if keyword_input:
      data = data[data['keywords'].isin(keyword_input)]

    # Filtering allergen products
    if allergen == 'Ya':
      data = data[data['allergen'] == 'Tidak']

    # Init a TF-IDF vectorizer
    tfidfvec = TfidfVectorizer()

    #  Fit data on processed keywords
    vec = tfidfvec.fit(data["keywords"])
    features = vec.transform(data["keywords"])

    # Transform user input data based on fitted model
    description_vector =  vec.transform([description])

    # Calculate cosine similarities between users processed input and keywords
    cos_sim = cosine_similarity(description_vector, features)

    # Add similarities to data frame
    data['similarity'] = cos_sim[0]

    # Sort data frame by similarities
    data.sort_values(by='similarity', ascending=False, inplace=True)

    data = data[(data['similarity'] > 0.1) & ((data['skin_type'].str.contains(res_st)) | (data['skin_type'] == 'semua'))]

    return data[['RATING', 'KATEGORI', 'GAMBAR', 'PRODUK', 'BRAND', 'DESKRIPSI', 'HARGA', 'similarity']]

print("Time taken: %s seconds" % (time.time() - start))