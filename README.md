# 🎬 Movie Recommender & Recommendation System

A modern, high-performance **Movie Recommender System** built with **FastAPI**, **Streamlit**, and **Machine Learning (TF-IDF Cosine Similarity)**, styled in a premium **Netflix-Inspired Cinema Theme**.

Created by **Amit Kanzariya**.

---

## ✨ Features

- **🍿 Netflix-Inspired Cinema Theme**: Dark mode `#0B0B0F` UI with translucent glassmorphism cards and Netflix Red `#E50914` accents.
- **🤖 Dual Recommendation Engine**:
  - **TF-IDF + Cosine Similarity**: Recommends similar movies based on content similarity from local datasets.
  - **Genre-Based Recommendations**: Uses TMDB API to discover movies within the same genre.
- **🔍 Smart Live Search & Autocomplete**: Real-time keyword search with interactive TMDB suggestions dropdown.
- **🔥 Quick Genre Filters**: One-click genre pills (`🔥 Action`, `😂 Comedy`, `🚀 Sci-Fi`, `💀 Horror`, `⚡ Superhero`, `🎨 Animation`) with high-contrast icons.
- **⭐ Saved Watchlist**: Interactive bookmarking system to save your favorite movies locally.
- **🎲 Surprise Me**: Random movie picker to discover unexpected film recommendations.
- **▶ Trailer Integration**: One-click direct link to official YouTube movie trailers.
- **⚡ Fast REST API**: Powered by FastAPI backend with CORS support and fallback endpoints.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python)
- **Backend API**: FastAPI + Uvicorn
- **Machine Learning**: Scikit-Learn (TF-IDF Vectorizer & Cosine Similarity), Pandas, NumPy
- **Data & APIs**: TMDB (The Movie Database) API, Scipy Sparse Matrices
- **HTTP Client**: HTTPX, Requests

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Amitkanzariya43-gif/Movie_Recommendation.git
cd Movie_Recommendation
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate

# macOS / Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
Copy `.env.example` to `.env` and add your **TMDB API Key**:
```bash
cp .env.example .env
```
Inside `.env`:
```env
TMDB_API_KEY=your_tmdb_api_key_here
```

---

## 🏃 Running the Application

### Step 1: Start FastAPI Backend
```bash
python -m uvicorn main:app --reload --port 8000
```
*API docs available at: `http://127.0.0.1:8000/docs`*

### Step 2: Start Streamlit Frontend
```bash
streamlit run app.py
```
*App will open automatically at: `http://localhost:8501`*

---

## 📁 Project Structure

```
Movie_Recommendation/
├── app.py                  # Streamlit Frontend (Netflix Theme & UI)
├── main.py                 # FastAPI Backend (Endpoints & ML Engine)
├── df.pkl                  # Processed DataFrame
├── indices.pkl             # Title-to-Index Map
├── tfidf_matrix.pkl        # TF-IDF Cosine Vector Matrix
├── tfidf.pkl               # TF-IDF Vectorizer
├── movies.ipynb            # Jupyter Notebook for Data Processing
├── requirements.txt        # Python Dependencies
├── .env.example            # Sample Environment Variables
├── .gitignore              # Git Ignore Rules
└── README.md               # Documentation
```

---

## 👤 Author

**Amit Kanzariya**  
GitHub: [@Amitkanzariya43-gif](https://github.com/Amitkanzariya43-gif)
