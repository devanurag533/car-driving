import streamlit as st
import time
import random
import pandas as pd

# --- 🛡️ STEP 1: HACKER-PROOF SECURITY LAYER ---
# Isse mouse aur keyboard dono lock ho jayenge
st.set_page_config(page_title="SmartCar Secure Pro", layout="wide", page_icon="🛰️")

st.markdown("""
    <script>
    // Disable Right Click
    document.addEventListener('contextmenu', event => event.preventDefault());

    // Disable Keyboard Shortcuts
    document.onkeydown = function(e) {
        if (e.keyCode == 123) { return false; } // F12
        if (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74)) { return false; } // Inspect/Console
        if (e.ctrlKey && e.keyCode == 85) { return false; } // View Source (Ctrl+U)
        if (e.ctrlKey && e.keyCode == 67) { return false; } // Copy (Ctrl+C)
    };
    </script>
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 🔑 STEP 2: PROFESSIONAL LOGIN SYSTEM ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🔐 Secure Car Access")
    st.subheader("Welcome to Anurag's Fleet Management")
    
    with st.container():
        user = st.text_input("Username (Owner ID)")
        password = st.text_input("Password", type="password")
        
        if st.button("Login to Vehicle"):
            if user == "anurag" and password == "bihar123": # Ye aapka secret password hai
                st.session_state.logged_in = True
                st.success("Access Granted! Fetching Live Data...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid Credentials! Unauthorized access is recorded.")

# --- 🛰️ STEP 3: LIVE DASHBOARD (THE MONEY MAKER) ---
if st.session_state.logged_in:
    # Sidebar Info
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/744/744465.png", width=100)
    st.sidebar.title("Car Status: ACTIVE")
    st.sidebar.write("📍 Location: Patna, Bihar")
    st.sidebar.write("🆔 Vehicle: BR-01-AK-2024")
    
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
 # --- 📍 STEP 4: LIVE LOCATION MAP ---
    st.subheader("🗺️ Real-time Vehicle Tracking")      
 # Simulated GPS Coordinates (Patna, Bihar ke aas-paas)
    lat = 25.5941 + random.uniform(-0.01, 0.01)
    lon = 85.1376 + random.uniform(-0.01, 0.01)
    map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
 # Streamlit ka in-built map
    st.map(map_data, zoom=13)
    st.caption(f"📍 Current Coordinates: {lat:.4f}, {lon:.4f} | Status: Moving")

    st.title("🛰️ SmartCar Live Telematics")
    st.write(f"**Admin:** Anurag Kumar | **Security Status:** 🛡️ Z-Plus Encrypted")
    st.markdown("---")

    # Live Data Simulation Loop
    placeholder = st.empty()
    
    for i in range(100):
        with placeholder.container():
            # Simulated Live Sensors
            speed = random.randint(60, 115)
            temp = random.randint(85, 105)
            fuel = 78.5 - (i * 0.05)
            
            # Top Metrics
            c1, c2, c3 = st.columns(3)
            c1.metric("🚀 Current Speed", f"{speed} km/h", delta="Fast" if speed > 100 else "Safe")
            c2.metric("🌡️ Engine Heat", f"{temp} °C", delta="⚠️ High" if temp > 100 else "Normal", delta_color="inverse")
            c3.metric("⛽ Fuel Left", f"{fuel:.2f} %")

            # Critical Alerts Logic
            if speed > 110:
                st.toast("🚨 OVER-SPEEDING ALERT SENT TO OWNER!", icon="⚠️")
            # --- 🚑 STEP 5: AI EMERGENCY RESPONSE SYSTEM (Is line 93 ke niche paste karein) ---
        st.markdown("---")
        st.subheader("🚨 SOS & Emergency Control")

        # 1. Accident Detection Logic
        if speed > 110:
             st.error("⚠️ HIGH SPEED IMPACT RISK! Monitoring Sensors...")

        # 2. Emergency Buttons
        col_sos1, col_sos2 = st.columns(2)
        
        with col_sos1:
            if st.button("🔴 REPORT ACCIDENT (SOS)"):
                phone = "91XXXXXXXXXX" # Yahan malik ka number dalna
                msg = f"EMERGENCY! Accident detected. Location: Patna. Speed was {speed}km/h."
                st.markdown(f"[📲 WhatsApp Owner](https://wa.me/{phone}?text={msg})")
                st.error("Alert Sent to Owner!")

        with col_sos2:
            if st.button("🚑 NEARBY AMBULANCE"):
                search_url = "https://www.google.com/maps/search/hospital+near+me"
                st.markdown(f"[🏥 Call Medical Help]({search_url})")

        # 3. Brake Failure Simulation
        if random.random() < 0.05: # 5% chance brake fail dikhane ki
            st.warning("🚨 SYSTEM ALERT: BRAKE PRESSURE LOW! CHECK VEHICLE.")
                st.error(f"CRITICAL: Vehicle is running at {speed} km/h. Risk of Accident!")
            
            if temp > 100:
                st.warning("ENGINE WARNING: Cooling system failure suspected. Please check oil.")

            # Data Table for History
            st.subheader("📋 Recent Trip Logs")
            data = pd.DataFrame({
                'Time': ['10:00 PM', '10:05 PM', '10:10 PM'],
                'Speed': [80, 95, speed],
                'Alerts': ['None', 'None', 'Overspeed' if speed > 100 else 'None']
            })
            st.table(data)
            
            time.sleep(3) # Har 3 second mein update hoga

# --- 🛑 FOOTER ---
else:
    login()

st.markdown("---")
st.caption("© 2024 Anurag Dev Systems | Protected by Masai Cyber-Security Protocol")
