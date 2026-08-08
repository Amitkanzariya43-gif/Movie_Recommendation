# Movie Recommender & Content Discovery System

An end-to-end Machine Learning and Web Application system for movie recommendations and content discovery. The system features a Content-Based Filtering engine based on TF-IDF Vectorization and Cosine Similarity, integrated with a FastAPI REST backend and a Netflix-inspired dark theme Streamlit frontend.

Created by **Amit Kanzariya**.

---

## Technical Overview

The architecture consists of three primary layers:

1. **Data Preprocessing & Machine Learning Pipeline** (`movies.ipynb`)
   - Preprocesses raw metadata from the TMDB dataset (45,000+ movies).
   - Extracts and normalizes structural fields (titles, overviews, taglines, and JSON-encoded genre strings).
   - Constructs a unified textual feature vector (`tags`) combining genre tokens, overview summaries, and promotional taglines.
   - Fits a Scikit-Learn `TfidfVectorizer` (with English stop-word removal) and computes pairwise Cosine Similarity matrices via linear kernels.
   - Serializes trained artifacts into compressed binary pickle formats (`df.pkl`, `indices.pkl`, `tfidf_matrix.pkl`, `tfidf.pkl`) for real-time inference.

2. **Backend REST API** (`main.py`)
   - Built with FastAPI and Uvicorn.
   - Loads serialized machine learning models into memory during startup for sub-millisecond similarity lookups.
   - Asynchronously communicates with external TMDB REST APIs via HTTPX for live movie metadata, poster imagery, and backdrop assets.
   - Provides bundled search endpoints returning content-based recommendations, genre fallback matches, and detailed movie profiles in single HTTP payloads.

3. **User Interface Application** (`app.py`)
   - Developed using Streamlit.
   - Custom styled with a dark slate background (`#0B0B0F`), translucent glassmorphism containers (`rgba(255, 255, 255, 0.10)`), and Netflix Red (`#E50914`) accents.
   - Implements single-page state routing (`home`, `details`, `watchlist`).
   - Integrated with interactive genre pills, bookmark state management, and direct trailer links.

---

## Core Features

- **Content-Based Filtering**: Recommends movies sharing plot, theme, and genre attributes using cosine similarity metrics.
- **Genre-Based Discovery**: Discovers top-rated movies sharing identical primary genre classifications.
- **Live Search & Autocomplete**: Real-time keyword search with instant suggestion parsing.
- **Quick Genre Filtering**: Streamlit pill components for instant single-click genre queries.
- **Interactive Watchlist**: Local session-state bookmarking to save and manage favorite movie selections.
- **Surprise Me Selector**: Random movie selection utility from active category feeds.
- **Media Integration**: Direct YouTube trailer search links and high-resolution TMDB poster imagery.

---

## Project Structure

```
Movie_Recommendation/
├── app.py                  # Streamlit frontend user interface
├── main.py                 # FastAPI backend service and model inference API
├── movies.ipynb            # Data cleaning, feature engineering, and model training notebook
├── df.pkl                  # Serialized cleaned movie DataFrame
├── indices.pkl             # Title-to-index mapping dictionary
├── tfidf_matrix.pkl        # Compressed sparse TF-IDF cosine similarity matrix
├── tfidf.pkl               # Serialized TfidfVectorizer instance
├── requirements.txt        # Python dependencies specification
├── .env.example            # Sample environment variables file
├── .gitignore              # Git version control ignore rules
└── README.md               # System documentation
```

---

## Installation & Setup

### Prerequisites

- Python 3.10 or higher
- Git version control
- TMDB API Key (obtainable from The Movie Database)

### 1. Repository Setup

```bash
git clone https://github.com/Amitkanzariya43-gif/Movie_Recommendation.git
cd Movie_Recommendation
```

### 2. Environment Setup

Create and activate a virtual environment:

```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On macOS / Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configuration

Create a `.env` file in the project root directory matching `.env.example`:

```env
TMDB_API_KEY=your_tmdb_api_key_here
```

---

## Running the Application

### 1. Start Backend API Server

Run the FastAPI backend using Uvicorn:

```bash
python -m uvicorn main:app --reload --port 8000
```

The interactive OpenAPI documentation will be accessible at:
`http://127.0.0.1:8000/docs`

### 2. Start Frontend Web Interface

In a separate terminal window, launch the Streamlit interface:

```bash
streamlit run app.py
```

The web application will open automatically at:
`http://localhost:8501`

---

## API Reference

| Endpoint | Method | Parameter | Description |
| :--- | :--- | :--- | :--- |
| `/` | GET | None | API root status and documentation metadata |
| `/health` | GET | None | Backend service health check |
| `/home` | GET | `category`, `limit` | Returns TMDB category feeds (popular, trending, top_rated, upcoming, now_playing) |
| `/tmdb/search` | GET | `query`, `page` | Queries TMDB search API for matching movie titles |
| `/movie/id/{tmdb_id}` | GET | `tmdb_id` | Returns complete metadata for a specific movie |
| `/recommend/tfidf` | GET | `title`, `top_n` | Executes TF-IDF cosine similarity lookup for a movie title |
| `/recommend/genre` | GET | `tmdb_id`, `limit` | Fetches recommendations based on primary genre matching |
| `/movie/search` | GET | `query`, `tfidf_top_n`, `genre_limit` | Returns combined search payload (details, TF-IDF recs, and genre recs) |

---

## Author

**Amit Kanzariya**  
GitHub: [Amitkanzariya43-gif](https://github.com/Amitkanzariya43-gif)
