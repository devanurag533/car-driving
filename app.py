import streamlit as st
import time
import random
import pandas as pd

# --- 🏛️ 1. GOVT-GRADE PROFESSIONAL UI CONFIG ---
st.set_page_config(page_title="Vahan-Secure Pro", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    div.stButton > button:first-child {
        background-color: #003366; color: white; border-radius: 8px;
        border: none; padding: 10px; font-weight: bold; width: 100%;
    }
    [data-testid="stMetricValue"] { color: #003366; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# --- 🔐 2. ADVANCED AUTH SYSTEM (Fixed Syntax) ---
if 'page' not in st.session_state: st.session_state.page = "login"
if 'owner_name' not in st.session_state: st.session_state.owner_name = "Anurag Kumar"
if 'car_number' not in st.session_state: st.session_state.car_number = "BR-01-AK-2026"
if 'user_password' not in st.session_state: st.session_state.user_password = "bihar123"

# --- 🔑 PAGE 1: LOGIN ---
if st.session_state.page == "login":
    st.title("🏛️ Vahan-Secure Dashboard")
    st.subheader("Government of India - Vehicle Telematics Portal")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        u = st.text_input("Officer/Owner ID")
        p = st.text_input("Secure Password", type="password")
        if st.button("Authorize Access"):
            # Yahan humne 'user_password' use kiya hai
            if u == "anurag" and p == st.session_state.user_password:
                st.session_state.page = "dashboard"
                st.rerun()
            else: 
                st.error("Access Denied: Invalid Credentials")
    
    with col2:
        st.info("🔐 Z-Plus Encryption Active")
        if st.button("Forgot Password?"):
            st.session_state.page = "forgot"
            st.rerun()
    st.stop()

# --- 🔑 PAGE 2: FORGOT PASSWORD ---
elif st.session_state.page == "forgot":
    st.title("🔓 Security Recovery")
    st.write(f"Recovery OTP will be sent to the device linked with: **{st.session_state.owner_name}**")
    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()
    st.stop()

# --- 🏠 PAGE 3: MAIN DASHBOARD ---
elif st.session_state.page == "dashboard":
    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg", width=60)
        st.title("Vahan Pro")
        st.markdown(f"👤 **Owner:** {st.session_state.owner_name}")
        st.markdown(f"🚘 **Vehicle:** `{st.session_state.car_number}`")
        st.markdown("---")
        
        menu = st.radio("Navigation:", ["📊 Analytics", "🗺️ Tracking", "🚨 SOS", "👤 Security"])
        
        st.markdown("---")
        if st.button("🔴 Logout"):
            st.session_state.page = "login"
            st.rerun()

    # Shared Data
    speed = random.randint(40, 110)
    lat, lon = 25.5941 + random.uniform(-0.01, 0.01), 85.1376 + random.uniform(-0.01, 0.01)

    if menu == "📊 Analytics":
        st.header("📊 Live Analytics")
        c1, c2, c3 = st.columns(3)
        c1.metric("Velocity", f"{speed} km/h")
        c2.metric("Fuel", "85%")
        c3.metric("Engine Health", "Good")
        
        st.subheader("📋 Trip Logs")
        st.table(pd.DataFrame({'Time':['10:00 PM','10:15 PM'], 'Status':['Safe','Moving'], 'Speed':[75, speed]}))

    elif menu == "🗺️ Tracking":
        st.header("🗺️ Satellite Tracking")
        st.map(pd.DataFrame({'lat':[lat], 'lon':[lon]}))
        st.success(f"📍 Location: Patna, Bihar")

    elif menu == "🚨 SOS":
        st.header("🚨 Crisis Management")
        if st.button("🔴 TRIGGER ACCIDENT SOS"):
            st.error("Police Dispatched to GPS Ground Zero!")

    elif menu == "👤 Security":
        st.header("👤 Security & Profile")
        st.session_state.owner_name = st.text_input("Update Name", st.session_state.owner_name)
        st.session_state.car_number = st.text_input("Update Car Number", st.session_state.car_number)
        new_p = st.text_input("Change Password", type="password")
        
        if st.button("Save Changes"):
            if new_p: 
                st.session_state.user_password = new_p
            st.success("Profile Securely Updated!")

st.markdown("---")
st.caption("© 2026 Anurag Dev Systems | IIT Patna x Masai Protocol")
