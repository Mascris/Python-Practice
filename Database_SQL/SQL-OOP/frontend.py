import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="CineVault Pro", page_icon="🎬", layout="wide")

# API URL (Where your FastAPI is running)
BASE_URL = "http://127.0.0.1:8000"

st.title("🎬 CineVault Professional Management")

# --- SIDEBAR NAVIGATION ---
menu = ["Home", "Login", "Sign Up", "Movies Store", "Rent/Return", "My History"]
choice = st.sidebar.selectbox("Menu", menu)

# --- HELPER: Handle Login State ---
if 'token' not in st.session_state:
    st.session_state['token'] = None
    st.session_state['user_email'] = ""

# --- LOGIN ---
if choice == "Login":
    st.subheader("Account Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        res = requests.post(f"{BASE_URL}/login", json={"email": email, "password": password})
        if res.status_code == 200:
            data = res.json()
            if data.get("status") == "success":
                st.session_state['token'] = data.get("access_token")
                st.session_state['user_email'] = email
                st.success(f"Welcome back! Your token is active.")
            else:
                st.error(data.get("error"))
        else:
            st.error("Connection failed.")

# --- SIGN UP ---
elif choice == "Sign Up":
    st.subheader("Create New Account")
    new_name = st.text_input("Full Name")
    new_email = st.text_input("Email")
    new_pass = st.text_input("Password", type="password")
    
    if st.button("Register"):
        payload = {"name": new_name, "email": new_email, "password": new_pass}
        res = requests.post(f"{BASE_URL}/users/add", json=payload)
        st.write(res.json().get("message", "Account Created!"))

# --- MOVIES STORE ---
elif choice == "Movies Store":
    st.subheader("Available Movies")
    res = requests.get(f"{BASE_URL}/movies/list")
    if res.status_code == 200:
        movies = res.json()
        st.table(movies) # This looks very professional!
    else:
        st.error("Could not fetch movies.")

# --- RENT/RETURN ---
elif choice == "Rent/Return":
    if not st.session_state['token']:
        st.warning("Please login first to rent movies.")
    else:
        st.info(f"Logged in as: {st.session_state['user_email']}")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("### Rent")
            m_title = st.text_input("Movie Title to Rent")
            if st.button("Confirm Rental"):
                payload = {"user_email": st.session_state['user_email'], "movie_title": m_title}
                res = requests.post(f"{BASE_URL}/rent", json=payload)
                st.write(res.json().get("message"))

        with col2:
            st.write("### Return")
            r_title = st.text_input("Movie Title to Return")
            if st.button("Confirm Return"):
                payload = {"user_email": st.session_state['user_email'], "movie_title": r_title}
                res = requests.post(f"{BASE_URL}/return", json=payload)
                st.write(res.json().get("message"))

# --- HISTORY ---
elif choice == "My History":
    if not st.session_state['user_email']:
        st.warning("Please login to see your history.")
    else:
        st.subheader(f"Rental History for {st.session_state['user_email']}")
        res = requests.get(f"{BASE_URL}/history/{st.session_state['user_email']}")
        if res.status_code == 200:
            st.json(res.json())
        else:
            st.error("Error fetching history.")

# --- HOME ---
else:
    st.write("Welcome to the CineVault Management System. Use the sidebar to navigate.")
    if st.session_state['token']:
        st.success("✅ You are authenticated.")
    else:
        st.info("👋 New here? Sign up to start renting.")
