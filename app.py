import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# 1. SETUP & DATASET (The "Backend" Brain)
@st.cache_data
def load_data():
    # In a real scenario, this would be 10,000+ songs. 
    # Features: Genre, Tempo (BPM), Energy (0-1), Language, Emotion
    data = {
        'song_id': [1, 2, 3, 4, 5, 6],
        'title': ['Starboy', 'Blinding Lights', 'Enjoy Enjaami', 'Arabic Kuthu', 'Lofi Rain', 'Midnight City'],
        'artist': ['The Weeknd', 'The Weeknd', 'Dhee ft. Arivu', 'Anirudh', 'Chill Beats', 'M83'],
        'genre': ['Pop', 'Synthwave', 'Folk-Pop', 'Kuthu', 'Lofi', 'Electronic'],
        'language': ['English', 'English', 'Tamil', 'Tamil', 'Instrumental', 'English'],
        'energy': [0.8, 0.9, 0.7, 0.95, 0.2, 0.85],
        'tempo': [186, 171, 120, 128, 80, 105],
        'emotion_score': [0.7, 0.8, 0.9, 0.9, 0.3, 0.75] # 0 = Sad, 1 = Happy
    }
    return pd.DataFrame(data)

def get_recommendations(current_song_title, df):
    # Select features for the algorithm
    features = ['energy', 'tempo', 'emotion_score']
    
    # Normalize tempo so it doesn't outweigh energy (ML Best Practice)
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[features] = scaler.fit_transform(df[features])
    
    # Convert Categorical (Genre/Language) to numbers using One-Hot Encoding
    # This allows the "Instagram Algorithm" to respect language and genre
    df_encoded = pd.get_dummies(df[['genre', 'language']])
    final_features = pd.concat([df_scaled[features], df_encoded], axis=1)
    
    # Calculate Similarity Matrix
    sim_matrix = cosine_similarity(final_features)
    
    # Find index of current song
    idx = df[df['title'] == current_song_title].index[0]
    
    # Get similarity scores and sort them
    distances = list(enumerate(sim_matrix[idx]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)
    
    # Return top 3 (excluding the current song itself)
    return [df.iloc[i[0]] for i in distances[1:4]]

# 2. UI/UX DESIGN (The Frontend)
st.set_page_config(page_title="VibeCheck AI", page_icon="🎵", layout="centered")

# Custom CSS for a "Dark Mode" Instagram feel
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #1DB954; color: white; }
    .song-card { padding: 20px; border-radius: 15px; background: #1e1e1e; margin-bottom: 10px; border-left: 5px solid #1DB954; }
    </style>
    """, unsafe_allow_html=True) # Changed from unsafe_allow_input

st.title("🎵 VibeCheck AI")
st.caption("Next-gen Recommendation Engine")

df = load_data()

# User Input
current_song = st.selectbox("💿 What are you listening to right now?", df['title'].tolist())

if st.button("Generate Next in Queue"):
    recommendations = get_recommendations(current_song, df)
    
    st.subheader("✨ Recommended for you")
    for rec in recommendations:
        with st.container():
            st.markdown(f"""
            <div class="song-card">
                <h4 style="margin:0;">{rec['title']}</h4>
                <p style="margin:0; color:#b3b3b3;">{rec['artist']} • {rec['genre']} • {rec['language']}</p>
            </div>
            """, unsafe_allow_html=True) # Changed from unsafe_allow_input

# Footer for your portfolio
st.markdown("---")
st.info("Built by Bharath vaaj A")