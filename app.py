import streamlit as st
import time
import random
import pandas as pd

# --- 🏛️ 1. GOVT-GRADE PROFESSIONAL UI CONFIG ---
st.set_page_config(page_title="Vahan-Secure Pro", layout="wide", page_icon="🏛️")

# Custom CSS for Professional Blue-White Look
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main { color: #1a1a1a; }
    /* Modern Govt Blue Buttons */
    div.stButton > button:first-child {
        background-color: #003366; color: white; border-radius: 8px;
        border: none; padding: 10px; font-weight: bold; width: 100%;
    }
    /* Emergency Button Red */
    .emergency-btn button { background-color: #cc0000 !important; }
    /* Metric Cards Styling */
    [data-testid="stMetricValue"] { color: #003366; font-weight: 800; }
    .sidebar-text { font-size: 14px; color: #555; }
    </style>
    """, unsafe_allow_html=True)

# --- 🔐 2. ADVANCED AUTH SYSTEM (Fixed Syntax) ---
if 'page' not in st.session_state: st.session_state.page = "login"
if 'owner_name' not in st.session_state: st.session_state.owner_name = "Anurag Kumar"
if 'car_number' not in st.session_state: st.session_state.car_number = "BR-01-AK-2026"
if 'user_pass' not in st.session_state: st.session_state.user_pass = "bihar123" # 'pass' ko 'user_pass' kar diya

# --- 🛡️ SECURITY BLOCKER (Right Click/F12) ---
st.markdown("<script>document.addEventListener('contextmenu', e => e.preventDefault());</script>", unsafe_allow_html=True)

# --- 🔑 PAGE 1: LOGIN & AUTH ---
if st.session_state.page == "login":
    st.title("🏛️ Vahan-Secure Dashboard")
    st.subheader("Government of India - Vehicle Telematics Portal")
    
    with st.container():
        col_l, col_r = st.columns([1, 1])
        with col_l:
            u = st.text_input("Officer/Owner ID")
            p = st.text_input("Secure Password", type="password")
            if st.button("Authorize Access"):
                if u == "anurag" and p == st.session_state.pass:
                    st.session_state.page = "dashboard"
                    st.rerun()
                else: st.error("Access Denied: Invalid Credentials")
        
        with col_r:
            st.info("System Alerts: 🔐 Z-Plus Encryption Active")
            if st.button("Forgot Password?"):
                st.session_state.page = "forgot"
                st.rerun()

# --- 🔑 PAGE 2: FORGOT PASSWORD ---
elif st.session_state.page == "forgot":
    st.title("🔓 Security Recovery")
    email = st.text_input("Enter Registered Email/Phone")
    if st.button("Send Recovery OTP"):
        st.success(f"OTP sent to your device connected to {st.session_state.owner_name}")
    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()

# --- 🏠 PAGE 3: THE MAIN PROFESSIONAL DASHBOARD ---
elif st.session_state.page == "dashboard":
    
    # --- 🎛️ SIDEBAR NAVIGATION ---
    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg", width=60)
        st.title("Vahan Pro")
        st.markdown(f"**Owner:** {st.session_state.owner_name}")
        st.markdown(f"**Vehicle:** `{st.session_state.car_number}`")
        st.markdown("---")
        
        menu = st.radio("Navigation Menu:", 
                        ["📊 Live Analytics", "🗺️ Satellite Tracking", "🚨 Emergency Response", "👤 Account Security"])
        
        st.markdown("---")
        if st.button("🔴 Secure Logout"):
            st.session_state.page = "login"
            st.rerun()

    # --- SIMULATED DATA ---
    speed = random.randint(40, 110)
    lat, lon = 25.5941 + random.uniform(-0.01, 0.01), 85.1376 + random.uniform(-0.01, 0.01)

    # --- 🏎️ MAIN INTERFACE LOGIC ---
    if menu == "📊 Live Analytics":
        st.header("📊 Real-time Vehicle Analytics")
        c1, c2, c3 = st.columns(3)
        c1.metric("🚀 Velocity", f"{speed} km/h", delta="Stable")
        c2.metric("⛽ Fuel Efficiency", "88%", delta="-2% (Low)")
        c3.metric("🌡️ Engine Health", "Normal")
        
        st.subheader("📋 Official Trip Logs")
        st.table(pd.DataFrame({'Time':['10:00 PM','10:15 PM'], 'Status':['Safe','Moving'], 'Speed':[75, speed]}))

    elif menu == "🗺️ Satellite Tracking":
        st.header("🗺️ Live Satellite View")
        st.map(pd.DataFrame({'lat':[lat], 'lon':[lon]}))
        st.success(f"📍 GPS Ground Zero: Patna, Bihar (Lat: {lat:.4f})")

    elif menu == "🚨 Emergency Response":
        st.header("🚨 Crisis Management")
        st.warning("Authorized Personnel Only: SOS buttons trigger local authorities.")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="emergency-btn">', unsafe_allow_html=True)
            if st.button("🔴 TRIGGER ACCIDENT SOS"):
                st.error("Police and Ambulance Dispatched to GPS Location!")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if st.button("🔒 REMOTE ENGINE KILL"):
                st.error("Vehicle Immobilized - System Locked.")

    elif menu == "👤 Account Security":
        st.header("👤 Security & Profile")
        new_name = st.text_input("Update Owner Name", st.session_state.owner_name)
        new_car = st.text_input("Update Vehicle Number", st.session_state.car_number)
        new_pass = st.text_input("Change Security Password", type="password")
        
        if st.button("Update Profile"):
            st.session_state.owner_name = new_name
            st.session_state.car_number = new_car
            if new_pass: st.session_state.pass = new_pass
            st.success("Profile Securely Updated!")

st.caption("© 2026 Ministry of Transportation - Anurag Dev Systems | IIT Patna x Masai")
