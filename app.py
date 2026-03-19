import streamlit as st
import time
import random
import pandas as pd

# --- 🛡️ 1. Z-PLUS SECURITY LAYER ---
st.set_page_config(page_title="SmartCar Multi-User", layout="wide", page_icon="🏎️")
st.markdown("""
    <script>
    document.addEventListener('contextmenu', event => event.preventDefault());
    document.onkeydown = function(e) {
        if (e.keyCode == 123 || (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74)) || (e.ctrlKey && e.keyCode == 85)) {
            return false;
        }
    };
    </script>
    """, unsafe_allow_html=True)

# --- 🔑 2. MULTI-USER LOGIN SYSTEM ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = None

if not st.session_state.logged_in:
    st.title("🔐 Secure Vehicle Login")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        if st.button("Login as Admin"):
            if user == "anurag" and password == "bihar123":
                st.session_state.logged_in = True
                st.session_state.user_role = "Admin"
                st.rerun()
            else: st.error("Invalid Admin Access!")
    with col_l2:
        if st.button("Login as User/Driver"):
            if user == "driver" and password == "drive123":
                st.session_state.logged_in = True
                st.session_state.user_role = "User"
                st.rerun()
            else: st.error("Invalid User Access!")
    st.stop()

# --- 🛰️ 3. DATA SIMULATION ---
speed = random.randint(40, 110)
fuel = random.uniform(30, 90)
lat, lon = 25.5941 + random.uniform(-0.01, 0.01), 85.1376 + random.uniform(-0.01, 0.01)

# --- 🎛️ 4. DYNAMIC SIDEBAR (Based on Role) ---
with st.sidebar:
    st.title("🎛️ Control Center")
    st.write(f"Logged in as: **{st.session_state.user_role}**")
    
    if st.session_state.user_role == "Admin":
        menu = st.radio("SELECT FEATURE:", ["🏠 Admin Dashboard", "🗺️ Live Tracking", "🚨 SOS System", "⚙️ Full Settings"])
    else:
        menu = st.radio("SELECT FEATURE:", ["🏠 My Driving Stats", "🗺️ My Location"])
    
    st.markdown("---")
    if st.button("🔴 Logout"):
        st.session_state.logged_in = False
        st.rerun()

# --- 🏎️ 5. PAGE LOGIC ---
if menu in ["🏠 Admin Dashboard", "🏠 My Driving Stats"]:
    st.title(f"🚀 {st.session_state.user_role} Dashboard")
    c1, c2 = st.columns(2)
    c1.metric("Current Speed", f"{speed} km/h")
    c2.metric("Fuel Remaining", f"{fuel:.1f} %")
    
    if st.session_state.user_role == "Admin" and speed > 100:
        st.error("🚨 ALERT: Driver is over-speeding!")

elif menu in ["🗺️ Live Tracking", "🗺️ My Location"]:
    st.title("🗺️ Vehicle Map")
    map_df = pd.DataFrame({'lat': [lat], 'lon': [lon]})
    st.map(map_df)

elif menu == "🚨 SOS System":
    st.title("🚨 Emergency SOS (Admin Only)")
    if st.button("🔴 SEND POLICE ALERT"):
        st.error("Police Notified with GPS Location!")

elif menu == "⚙️ Full Settings":
    st.title("⚙️ Admin Settings")
    st.toggle("Lock Vehicle Engine")
    st.toggle("Disable Fuel Supply")

st.caption("© 2026 Anurag Dev Systems | IIT Patna x Masai Protocol")
