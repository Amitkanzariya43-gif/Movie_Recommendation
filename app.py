import requests
import streamlit as st
import random

TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(
    page_title="Movie Recommender | Cinema Edition",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: #FFFFFF !important;
}

.stApp {
    background: 
        radial-gradient(circle at 20% 0%, rgba(229, 9, 20, 0.18) 0%, transparent 40%),
        radial-gradient(circle at 80% 100%, rgba(255, 77, 79, 0.12) 0%, transparent 45%),
        #0B0B0F !important;
    color: #FFFFFF !important;
}

.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1400px !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, 0.10) !important;
    backdrop-filter: blur(16px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
    border: 1px solid rgba(255, 255, 255, 0.20) !important;
    border-radius: 16px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    padding: 0.9rem !important;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #E50914 !important;
    box-shadow: 0 12px 35px 0 rgba(229, 9, 20, 0.35) !important;
    transform: translateY(-3px) !important;
}

section[data-testid="stSidebar"] {
    background: rgba(11, 11, 15, 0.92) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.15) !important;
}

.stTextInput input, div[data-baseweb="select"] > div {
    background: rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.20) !important;
    border-radius: 12px !important;
    color: #FFFFFF !important;
    font-size: 0.98rem !important;
    transition: all 0.25s ease !important;
}

.stTextInput input:focus, div[data-baseweb="select"]:focus-within {
    border-color: #E50914 !important;
    box-shadow: 0 0 20px rgba(229, 9, 20, 0.45) !important;
}

.stButton button {
    background: linear-gradient(135deg, #E50914 0%, #FF4D4F 100%) !important;
    backdrop-filter: blur(12px) !important;
    border: none !important;
    border-radius: 10px !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    padding: 0.4rem 0.5rem !important;
    white-space: nowrap !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 15px rgba(229, 9, 20, 0.35) !important;
    min-height: 38px !important;
    height: 38px !important;
    width: 100% !important;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.4) !important;
}

.stButton button:hover {
    background: linear-gradient(135deg, #B9090B 0%, #E50914 100%) !important;
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 8px 25px rgba(229, 9, 20, 0.6) !important;
}

div[data-testid="stPills"] button, div[data-testid="stPills"] [role="option"], div[data-testid="stWidgetLabel"] {
    color: #FFFFFF !important;
}

div[data-testid="stPills"] button, div[data-testid="stPills"] [role="option"] {
    background: rgba(255, 255, 255, 0.08) !important;
    border: 1px solid rgba(255, 255, 255, 0.20) !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    border-radius: 20px !important;
    padding: 0.4rem 0.9rem !important;
    transition: all 0.25s ease !important;
}

div[data-testid="stPills"] button[aria-selected="true"], div[data-testid="stPills"] [role="option"][aria-selected="true"] {
    background: linear-gradient(135deg, #E50914 0%, #FF4D4F 100%) !important;
    border-color: #E50914 !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 15px rgba(229, 9, 20, 0.45) !important;
}

div[data-testid="stPills"] button:hover, div[data-testid="stPills"] [role="option"]:hover {
    border-color: #E50914 !important;
    background: rgba(255, 255, 255, 0.15) !important;
}

a[data-testid="stLinkButton"] {
    background: linear-gradient(135deg, #E50914 0%, #FF4D4F 100%) !important;
    border-radius: 10px !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    text-decoration: none !important;
    box-shadow: 0 4px 15px rgba(229, 9, 20, 0.4) !important;
    min-height: 38px !important;
    height: 38px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.4) !important;
}

div[data-testid="stImage"] img {
    border-radius: 12px !important;
    transition: transform 0.35s ease !important;
}

div[data-testid="stImage"] img:hover {
    transform: scale(1.03) !important;
}

h1, h2, h3, h4 {
    color: #FFFFFF !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em !important;
}

.hero-title {
    font-family: 'Bebas Neue', 'Outfit', sans-serif !important;
    background: linear-gradient(135deg, #FFFFFF 30%, #FF4D4F 70%, #E50914 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3.4rem;
    letter-spacing: 0.05em !important;
    margin-bottom: 0.1rem;
}

.hero-subtitle {
    color: #B3B3B3 !important;
    font-size: 1.05rem;
    margin-bottom: 1.2rem;
}

.movie-title-card {
    font-size: 0.92rem;
    font-weight: 600;
    line-height: 1.25rem;
    height: 2.5rem;
    overflow: hidden;
    color: #FFFFFF;
    margin-top: 0.5rem;
    text-align: center;
}

.secondary-text {
    color: #B3B3B3 !important;
    font-size: 0.9rem !important;
}

.no-poster {
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    color: #B3B3B3;
    font-size: 0.9rem;
}

.glass-footer {
    margin-top: 4rem;
    padding: 1.8rem 1rem;
    background: rgba(255, 255, 255, 0.10);
    backdrop-filter: blur(18px) saturate(180%);
    -webkit-backdrop-filter: blur(18px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.20);
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
}

.glass-footer-text {
    font-size: 1.15rem;
    font-weight: 700;
    color: #FFFFFF;
    letter-spacing: 0.03em;
}

.glass-footer-author {
    background: linear-gradient(135deg, #FF4D4F 0%, #E50914 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}

.glass-footer-sub {
    color: #B3B3B3;
    font-size: 0.88rem;
    margin-top: 0.4rem;
}

.metric-pill {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 12px;
    padding: 0.6rem 1rem;
    text-align: center;
}

.metric-pill-label {
    color: #B3B3B3;
    font-size: 0.8rem;
    font-weight: 500;
}

.metric-pill-value {
    color: #FFFFFF;
    font-size: 1.1rem;
    font-weight: 700;
    margin-top: 0.2rem;
}
</style>
""",
    unsafe_allow_html=True,
)

if "view" not in st.session_state:
    st.session_state.view = "home"
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None
if "watchlist" not in st.session_state:
    st.session_state.watchlist = {}
if "genre_query" not in st.session_state:
    st.session_state.genre_query = None

qp_view = st.query_params.get("view")
qp_id = st.query_params.get("id")
if qp_view in ("home", "details", "watchlist"):
    st.session_state.view = qp_view
if qp_id:
    try:
        st.session_state.selected_tmdb_id = int(qp_id)
        st.session_state.view = "details"
    except:
        pass


def goto_home():
    st.session_state.view = "home"
    st.session_state.genre_query = None
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()


def goto_watchlist():
    st.session_state.view = "watchlist"
    st.query_params["view"] = "watchlist"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()


def goto_details(tmdb_id: int):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = int(tmdb_id)
    st.query_params["view"] = "details"
    st.query_params["id"] = str(int(tmdb_id))
    st.rerun()


def toggle_watchlist(movie_card: dict):
    tmdb_id = movie_card.get("tmdb_id")
    if not tmdb_id:
        return
    if tmdb_id in st.session_state.watchlist:
        del st.session_state.watchlist[tmdb_id]
        st.toast("Removed from Watchlist", icon="🗑️")
    else:
        st.session_state.watchlist[tmdb_id] = movie_card
        st.toast("Saved to Watchlist! ⭐", icon="⭐")
    st.rerun()


LOCAL_API_BASE = "http://127.0.0.1:8000"
CLOUD_API_BASE = "https://movie-recommendation-uzo1.onrender.com"

@st.cache_data(ttl=30)
def api_get_json(path: str, params: dict | None = None):
    # 1. Try local backend first
    try:
        r = requests.get(f"{LOCAL_API_BASE}{path}", params=params, timeout=2.5)
        if r.status_code < 400:
            return r.json(), None
    except Exception:
        pass

    # 2. Fallback to remote cloud backend (Render)
    try:
        r = requests.get(f"{CLOUD_API_BASE}{path}", params=params, timeout=45)
        if r.status_code >= 400:
            return None, f"HTTP {r.status_code}: {r.text[:300]}"
        return r.json(), None
    except requests.exceptions.Timeout:
        return None, "The cloud server is waking up from sleep. Please refresh in a few seconds, or start your local server with 'python -m uvicorn main:app --reload'!"
    except Exception as e:
        return None, f"Request failed: {e}"


def poster_grid(cards, cols=6, key_prefix="grid"):
    if not cards:
        st.info("No movies to show.")
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0
    for r in range(rows):
        colset = st.columns(cols)
        for c in range(cols):
            if idx >= len(cards):
                break
            m = cards[idx]
            idx += 1

            tmdb_id = m.get("tmdb_id")
            title = m.get("title", "Untitled")
            poster = m.get("poster_url")
            is_saved = tmdb_id in st.session_state.watchlist if tmdb_id else False

            with colset[c]:
                with st.container(border=True):
                    if poster:
                        st.image(poster, use_container_width=True)
                    else:
                        st.markdown("<div class='no-poster'>🖼️ No Poster</div>", unsafe_allow_html=True)

                    c1, c2 = st.columns([3.2, 1.2])
                    with c1:
                        if st.button("▶ Open", key=f"{key_prefix}_{r}_{c}_{idx}_{tmdb_id}", use_container_width=True):
                            if tmdb_id:
                                goto_details(tmdb_id)
                    with c2:
                        bookmark_icon = "✔" if is_saved else "⭐"
                        if st.button(bookmark_icon, key=f"fav_{key_prefix}_{r}_{c}_{idx}_{tmdb_id}", use_container_width=True):
                            toggle_watchlist(m)

                    st.markdown(
                        f"<div class='movie-title-card'>{title}</div>", unsafe_allow_html=True
                    )


def to_cards_from_tfidf_items(tfidf_items):
    cards = []
    for x in tfidf_items or []:
        tmdb = x.get("tmdb") or {}
        if tmdb.get("tmdb_id"):
            cards.append(
                {
                    "tmdb_id": tmdb["tmdb_id"],
                    "title": tmdb.get("title") or x.get("title") or "Untitled",
                    "poster_url": tmdb.get("poster_url"),
                }
            )
    return cards


def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 24):
    keyword_l = keyword.strip().lower()

    if isinstance(data, dict) and "results" in data:
        raw = data.get("results") or []
        raw_items = []
        for m in raw:
            title = (m.get("title") or "").strip()
            tmdb_id = m.get("id")
            poster_path = m.get("poster_path")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": f"{TMDB_IMG}{poster_path}" if poster_path else None,
                    "release_date": m.get("release_date", ""),
                }
            )

    elif isinstance(data, list):
        raw_items = []
        for m in data:
            tmdb_id = m.get("tmdb_id") or m.get("id")
            title = (m.get("title") or "").strip()
            poster_url = m.get("poster_url")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": poster_url,
                    "release_date": m.get("release_date", ""),
                }
            )
    else:
        return [], []

    matched = [x for x in raw_items if keyword_l in x["title"].lower()]
    final_list = matched if matched else raw_items

    suggestions = []
    for x in final_list[:10]:
        year = (x.get("release_date") or "")[:4]
        label = f"{x['title']} ({year})" if year else x["title"]
        suggestions.append((label, x["tmdb_id"]))

    cards = [
        {"tmdb_id": x["tmdb_id"], "title": x["title"], "poster_url": x["poster_url"]}
        for x in final_list[:limit]
    ]
    return suggestions, cards


def render_footer():
    st.markdown(
        """
        <div class="glass-footer">
            <div class="glass-footer-text">
                <span class="glass-footer-author">Created by Amit Kanzariya</span>
            </div>
            <div class="glass-footer-sub">
                Movie Recommender System &bull; Cinema Edition
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


with st.sidebar:
    st.markdown("## 🎬 Navigation")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        if st.button("🏠 Home", use_container_width=True):
            goto_home()
    with col_s2:
        fav_count = len(st.session_state.watchlist)
        if st.button(f"⭐ Saved ({fav_count})", use_container_width=True):
            goto_watchlist()

    st.markdown("---")
    st.markdown("### ⚙️ Feed Filter")
    home_category = st.selectbox(
        "Category",
        ["trending", "popular", "top_rated", "now_playing", "upcoming"],
        index=0,
    )
    grid_cols = st.slider("Grid Columns", 4, 8, 6)

    st.markdown("---")
    st.markdown("### 🎲 Surprise Me")
    if st.button("🎲 Random Movie Picker", use_container_width=True):
        home_cards, err = api_get_json("/home", params={"category": home_category, "limit": 20})
        if home_cards and isinstance(home_cards, list) and len(home_cards) > 0:
            rand_m = random.choice(home_cards)
            if rand_m.get("tmdb_id"):
                goto_details(rand_m["tmdb_id"])
        else:
            st.toast("Could not load random movie", icon="⚠️")

    st.markdown("---")
    st.markdown("### 📊 System Status")
    with st.container(border=True):
        st.markdown(f"**⭐ Saved:** {len(st.session_state.watchlist)} movies")
        st.markdown(f"**🎬 Active Feed:** {home_category.replace('_', ' ').title()}")
        st.markdown("**🤖 AI Engine:** TF-IDF + TMDB")

    if st.session_state.watchlist:
        st.markdown("---")
        if st.button("🧹 Clear Watchlist", use_container_width=True):
            st.session_state.watchlist = {}
            st.toast("Watchlist cleared!", icon="🧹")
            st.rerun()

st.markdown(
    """
    <div>
        <h1 class="hero-title">🎬 MOVIE RECOMMENDER</h1>
        <p class="hero-subtitle">Discover tailored cinematic gems with intelligent machine learning & TMDB</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.divider()

if st.session_state.view == "watchlist":
    st.markdown("### ⭐ My Saved Watchlist")
    saved_cards = list(st.session_state.watchlist.values())
    if not saved_cards:
        st.info("Your Watchlist is currently empty! Click ⭐ on any movie card to save it here.")
    else:
        st.caption(f"Showing {len(saved_cards)} saved movies")
        poster_grid(saved_cards, cols=grid_cols, key_prefix="watchlist_grid")
    
    render_footer()

elif st.session_state.view == "home":
    typed = st.text_input(
        "🔍 Search Movie Title", placeholder="Type keywords: Avengers, Batman, Spider-Man, Inception..."
    )

    genre_options = ["🔥 Action", "😂 Comedy", "🚀 Sci-Fi", "💀 Horror", "⚡ Superhero", "🎨 Animation"]
    selected_pill = st.pills(
        "Quick Genre Search:",
        options=genre_options,
        selection_mode="single",
    )
    if selected_pill:
        genre_map = {
            "🔥 Action": "action",
            "😂 Comedy": "comedy",
            "🚀 Sci-Fi": "science fiction",
            "💀 Horror": "horror",
            "⚡ Superhero": "spider-man",
            "🎨 Animation": "animation",
        }
        st.session_state.genre_query = genre_map.get(selected_pill)

    search_term = typed.strip() or st.session_state.genre_query

    st.divider()

    if search_term:
        data, err = api_get_json("/tmdb/search", params={"query": search_term})

        if err or data is None:
            st.error(f"Search failed: {err}")
        else:
            suggestions, cards = parse_tmdb_search_to_cards(
                data, search_term, limit=24
            )

            if suggestions:
                labels = ["-- Select a movie suggestion --"] + [s[0] for s in suggestions]
                selected = st.selectbox("Suggestions Dropdown", labels, index=0)

                if selected != "-- Select a movie suggestion --":
                    label_to_id = {s[0]: s[1] for s in suggestions}
                    goto_details(label_to_id[selected])
            else:
                st.info("No suggestions found. Try another keyword.")

            st.markdown(f"### 🍿 Results for '{search_term}'")
            poster_grid(cards, cols=grid_cols, key_prefix="search_results")

        st.stop()

    st.markdown(f"### 🏠 {home_category.replace('_',' ').title()} Movies")

    home_cards, err = api_get_json(
        "/home", params={"category": home_category, "limit": 24}
    )
    if err or not home_cards:
        st.error(f"Home feed failed: {err or 'Unknown error'}")
        st.stop()

    poster_grid(home_cards, cols=grid_cols, key_prefix="home_feed")
    render_footer()

elif st.session_state.view == "details":
    tmdb_id = st.session_state.selected_tmdb_id
    if not tmdb_id:
        st.warning("No movie selected.")
        if st.button("← Back to Home"):
            goto_home()
        st.stop()

    a, b = st.columns([3, 1])
    with a:
        st.markdown("### 📄 Movie Details")
    with b:
        if st.button("← Back to Home", use_container_width=True):
            goto_home()

    data, err = api_get_json(f"/movie/id/{tmdb_id}")
    if err or not data:
        st.error(f"Could not load details: {err or 'Unknown error'}")
        st.stop()

    movie_card_obj = {
        "tmdb_id": tmdb_id,
        "title": data.get("title", ""),
        "poster_url": data.get("poster_url"),
    }
    is_saved = tmdb_id in st.session_state.watchlist

    left, right = st.columns([1, 2.4], gap="large")

    with left:
        with st.container(border=True):
            if data.get("poster_url"):
                st.image(data["poster_url"], use_container_width=True)
            else:
                st.write("🖼️ No poster")

            btn_label = "✔ Saved in Watchlist" if is_saved else "⭐ Save to Watchlist"
            if st.button(btn_label, use_container_width=True):
                toggle_watchlist(movie_card_obj)

    with right:
        with st.container(border=True):
            st.markdown(f"## {data.get('title','')}")
            
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(
                    f"<div class='metric-pill'><div class='metric-pill-label'>🗓️ Release</div><div class='metric-pill-value'>{data.get('release_date') or '-'}</div></div>",
                    unsafe_allow_html=True
                )
            with m2:
                genres = ", ".join([g["name"] for g in data.get("genres", [])[:2]]) or "-"
                st.markdown(
                    f"<div class='metric-pill'><div class='metric-pill-label'>🎭 Genres</div><div class='metric-pill-value'>{genres}</div></div>",
                    unsafe_allow_html=True
                )
            with m3:
                vote = data.get("vote_average", "N/A")
                st.markdown(
                    f"<div class='metric-pill'><div class='metric-pill-label'>⭐ TMDB Rating</div><div class='metric-pill-value'>{vote}</div></div>",
                    unsafe_allow_html=True
                )

            st.markdown("---")
            st.markdown("### Overview")
            st.write(data.get("overview") or "No overview available.")
            
            title_query = data.get("title", "").replace(" ", "+")
            st.link_button("▶ Watch Official Trailer on YouTube", f"https://www.youtube.com/results?search_query={title_query}+official+trailer", use_container_width=True)

    if data.get("backdrop_url"):
        st.markdown("#### 🖼️ Backdrop")
        st.image(data["backdrop_url"], use_container_width=True)

    st.divider()
    st.markdown("### ✨ Recommended For You")

    title = (data.get("title") or "").strip()
    if title:
        bundle, err2 = api_get_json(
            "/movie/search",
            params={"query": title, "tfidf_top_n": 12, "genre_limit": 12},
        )

        if not err2 and bundle:
            st.markdown("#### 🔎 Similar Movies (TF-IDF Match)")
            poster_grid(
                to_cards_from_tfidf_items(bundle.get("tfidf_recommendations")),
                cols=grid_cols,
                key_prefix="details_tfidf",
            )

            st.markdown("#### 🎭 More Like This (Genre Match)")
            poster_grid(
                bundle.get("genre_recommendations", []),
                cols=grid_cols,
                key_prefix="details_genre",
            )
        else:
            st.info("Showing Genre recommendations (fallback).")
            genre_only, err3 = api_get_json(
                "/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18}
            )
            if not err3 and genre_only:
                poster_grid(
                    genre_only, cols=grid_cols, key_prefix="details_genre_fallback"
                )
            else:
                st.warning("No recommendations available right now.")
    else:
        st.warning("No title available to compute recommendations.")

    render_footer()