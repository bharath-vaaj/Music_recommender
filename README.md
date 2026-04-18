# VibeCheck AI 🎵
### A Personal Music Recommendation Engine

VibeCheck AI is a lightweight, content-based recommendation system designed to mimic the behavior of modern social media algorithms like Instagram and Spotify. It suggests the "next song" based on the mathematical similarity of the current track's genre, language, and emotional metadata.

---

## 🚀 Project Overview
This project uses **Cosine Similarity** to calculate the distance between songs in a multi-dimensional feature space. By analyzing features like energy, tempo, and emotion scores, the algorithm provides personalized recommendations that maintain the "vibe" of the current listening session.

## ✨ Features
* **Vector-Based Recommendation:** Uses Scikit-Learn to compute similarities between tracks.
* **Feature Normalization:** Implements `MinMaxScaler` to ensure different scales (like Tempo vs. Energy) are weighted fairly.
* **Localized Context:** Support for multiple languages (English, Tamil, etc.) and genres.
* **Sleek UI/UX:** A custom-styled dark mode interface built with Streamlit.
* **Zero-Cost:** Runs entirely on local data and open-source libraries—no expensive API keys required.

## 🧠 How the Algorithm Works
The backend calculates the **Cosine Similarity** between song vectors. It treats every song as a point in space; the smaller the angle between two points, the more similar the songs are.



## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **Frontend:** Streamlit
* **Machine Learning:** Scikit-Learn, Pandas
* **Styling:** Custom CSS (Instagram-inspired Dark Mode)



## 👤 Author
* **Bharath vaaj A**
