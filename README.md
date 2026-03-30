🛡️ NetSafe_AI: AI-Driven Network Threat Detection
NetSafe_AI is an advanced Network Intrusion Detection System (NIDS) that leverages Machine Learning to identify malicious traffic patterns in real-time. While traditional security tools rely on static signatures, NetSafe_AI uses a Random Forest Classifier to detect behavioral anomalies such as Brute Force attacks and Data Exfiltration.

This project serves as the "Network Layer" defense in a multi-layer security ecosystem, complementing Safe-Surf AI (Application Layer defense).

🚀 Key Features
.Multi-Vector Detection: Specifically trained to identify high-login-attempt patterns (Brute Force) and high-volume data transfers with low login counts (Data Exfiltration).

.Live Packet Sniffing: Integrated with Scapy to capture and analyze real-time traffic from the local network interface.

.Interactive Dashboard: Built with Streamlit, featuring manual simulation sliders, "One-Click" attack scenarios, and live packet logs.

.High-Accuracy ML Model: Utilizes a serialized Random Forest model (.pkl) achieving near-perfect precision on balanced synthetic network datasets.

🏗️ Project Architecture
NetSafe_AI operates across the Network and Transport layers (Layers 3 & 4 of the OSI model), focusing on metadata rather than content.

1. Data Generation: Custom Python scripts generate diverse traffic profiles (Normal vs. Malicious).

2. Model Training: Scikit-learn processes features like duration, bytes_sent, bytes_received, and login_attempts.

3. Real-Time Inference: The Streamlit frontend captures live data or manual inputs and passes them through the trained "brain" for instant classification.

🛠️ Tech Stack
.Language: Python 3.x

.Machine Learning: Scikit-learn (Random Forest), Pandas, NumPy, Joblib

.Network Security: Scapy (Packet Sniffing & Header Analysis)

.Frontend/UI: Streamlit

.Development: VS Code, Git

📋 Installation & Setup
1. Clone the repository:

Bash
git clone https://github.com/yourusername/NetSafe_AI.git
cd NetSafe_AI
2. Create a Virtual Environment:

Bash
python -m venv .venv
.venv\Scripts\activate  # Windows
3. Install Dependencies:

Bash
pip install -r requirements.txt
4. Install Npcap (For Live Sniffing):
Ensure Npcap is installed on your Windows machine in "WinPcap API-compatible Mode."

🎮 Usage
Option 1: Manual Simulation
Use the interactive sliders to adjust network parameters. Click "Run AI Analysis" to see if the pattern is flagged. Use the Preset Buttons to quickly load known attack profiles.

Option 2: Live Network Scan
(Requires Administrator Privileges)
Click "Start Live Capture" to listen to 5 seconds of real network traffic. The system will display the packet log (Source/Dest IP) and provide a security status update.

📈 Future Roadmap
.Feature Expansion: Adding detection for DDoS (UDP Flood) and Port Scanning.

.Visual Analytics: Integrating Plotly to show real-time traffic spikes and threat probability graphs.

.Cloud Integration: Sending alerts to a centralized dashboard via Webhooks.

👤 Author
Dikshant Sharma B.Tech in Artificial Intelligence & Machine Learning 📍 Rewari, Haryana, India