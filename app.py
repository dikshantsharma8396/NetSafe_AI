import streamlit as st
import joblib
import pandas as pd
import time
from scapy.all import sniff, IP

# 1. Setup Page
st.set_page_config(page_title="NetSafe_AI Dashboard", page_icon="🛡️", layout="wide")
st.title("🛡️ NetSafe_AI: Multi-Layer Security")

# 2. Load the AI Brain
model = joblib.load('models/netsafe_model.pkl')

# 3. Initialize Session State for Manual Inputs
if 'dur_val' not in st.session_state:
    st.session_state.dur_val = 5
if 'sent_val' not in st.session_state:
    st.session_state.sent_val = 250
if 'rec_val' not in st.session_state:
    st.session_state.rec_val = 300
if 'login_val' not in st.session_state:
    st.session_state.login_val = 1

# 4. Create the Sidebar (The Menu)
st.sidebar.image("https://img.icons8.com/fluency/96/shield.png", width=100)
st.sidebar.title("Security Control")
option = st.sidebar.radio("Choose how to scan:", ("Option 1: Manual Input", "Option 2: Live Network Scan"))
st.sidebar.info("This AI model is trained to detect Brute Force and Data Exfiltration attacks.")

# --- OPTION 1: MANUAL INPUT ---
if option == "Option 1: Manual Input":
    st.subheader("🧪 Manual Threat Testing")
    st.write("Slide the bars to simulate different network scenarios.")

    # --- EXAMPLE BUTTONS ---
    col_ex1, col_ex2 = st.columns(2)
    if col_ex1.button("💡 Load Example: Normal Browsing"):
        st.session_state.dur_val, st.session_state.sent_val = 5, 250
        st.session_state.rec_val, st.session_state.login_val = 300, 1
        st.rerun()

    if col_ex2.button("⚠️ Load Example: Data Exfiltration"):
        st.session_state.dur_val, st.session_state.sent_val = 200, 45000
        st.session_state.rec_val, st.session_state.login_val = 500, 1
        st.rerun()
    
    st.divider()

    # --- INPUT SLIDERS (UX IMPROVEMENT) ---
    col1, col2 = st.columns(2)
    with col1:
        dur = st.slider("Connection Duration (seconds)", 0, 500, st.session_state.dur_val, 
                        help="How long the device stayed connected.")
        b_sent = st.slider("Data Sent (Bytes)", 0, 100000, st.session_state.sent_val, 
                           help="Amount of data leaving the network.")
    with col2:
        b_rec = st.slider("Data Received (Bytes)", 0, 100000, st.session_state.rec_val, 
                          help="Amount of data entering the network.")
        logins = st.slider("Login Attempts", 0, 50, st.session_state.login_val, 
                           help="Failed or successful login attempts detected.")

    if st.button("Run AI Analysis", use_container_width=True):
        # Data preparation
        test_data = pd.DataFrame([[dur, b_sent, b_rec, logins]], 
                                 columns=['duration', 'bytes_sent', 'bytes_received', 'login_attempts'])
        prediction = model.predict(test_data)
        
        st.write("### AI Verdict:")
        if prediction[0] == 0:
            st.balloons()
            st.success("#### ✅ SECURE: The traffic pattern appears safe and normal.")
            st.progress(10) # Low risk
        else:
            st.error("#### 🚨 THREAT DETECTED: This pattern matches known attack vectors!")
            st.progress(95) # High risk
    
    with st.expander("❓ How to read these results?"):
        st.write("- **Normal:** Short connections with balanced data.")
        st.write("- **Brute Force:** High login attempts.")
        st.write("- **Exfiltration:** Extremely high 'Bytes Sent' with long duration.")

# --- OPTION 2: LIVE NETWORK SCAN ---
elif option == "Option 2: Live Network Scan":
    st.subheader("📡 Live Infrastructure Monitoring")
    st.write("Sniffing real-time packets from your network interface.")

    if st.button("Start Live Capture", use_container_width=True, type="primary"):
        # Initialize variables so they exist outside the status block
        packets = []
        packet_list = []
        result = [0]

        with st.status("Listening to Network Interface...", expanded=True) as status:
            st.write("Sniffing packets...")
            packets = sniff(count=50, timeout=5)
            st.write("Processing packet headers...")
            
            # --- PACKET DATA COLLECTION ---
            for p in packets:
                if p.haslayer(IP):
                    packet_list.append({
                        "Source IP": p[IP].src,
                        "Destination IP": p[IP].dst,
                        "Length": len(p),
                        "Protocol": p[IP].proto
                    })
            
            # Logic calculation
            total_bytes = sum(len(p) for p in packets)
            live_data = pd.DataFrame([[5, total_bytes/2, total_bytes/2, 1]], 
                                     columns=['duration', 'bytes_sent', 'bytes_received', 'login_attempts'])
            result = model.predict(live_data)
            status.update(label="Scan Complete!", state="complete", expanded=False)

        # --- UPDATED LOC: Displaying results OUTSIDE the status block ---
        st.divider() 
        
        if packet_list:
            st.write("### 📜 Captured Packet Log")
            # Changed to st.dataframe to allow the user to scroll through the packets
            st.dataframe(pd.DataFrame(packet_list), use_container_width=True)
            
        # Final Result Display
        if result[0] == 0:
            st.info("### 🟢 Status: Network is Secure")
            st.write(f"Scan analyzed {len(packets)} packets. No anomalies found.")
        else:
            st.warning("### 🔴 Status: Unusual Traffic Spotted")
            st.write("The volume of traffic detected is higher than normal benchmarks.")