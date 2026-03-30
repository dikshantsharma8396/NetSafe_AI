import pandas as pd
import numpy as np
import os

# Create the data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

print("Step 1: Generating IMPROVED synthetic network traffic data...")

# We will create 1,500 rows to make the AI even smarter
# 500 Normal, 500 Brute Force, 500 Data Exfiltration
sub_size = 500 

# --- 1. NORMAL TRAFFIC ---
# Fast connections, low data, 1 login
normal_traffic = {
    'duration': np.random.uniform(1, 10, sub_size),
    'bytes_sent': np.random.uniform(100, 500, sub_size),
    'bytes_received': np.random.uniform(100, 500, sub_size),
    'login_attempts': np.ones(sub_size),
    'label': 0 
}

# --- 2. ATTACK TYPE A: BRUTE FORCE ---
# Long duration, many login attempts, moderate data
brute_force = {
    'duration': np.random.uniform(30, 100, sub_size),
    'bytes_sent': np.random.uniform(500, 1500, sub_size),
    'bytes_received': np.random.uniform(500, 1500, sub_size),
    'login_attempts': np.random.randint(5, 30, sub_size),
    'label': 1 
}

# --- 3. ATTACK TYPE B: DATA EXFILTRATION (The "Thief") ---
# Long duration, HUGE bytes_sent, but only 1 login attempt
data_exfiltration = {
    'duration': np.random.uniform(100, 400, sub_size),
    'bytes_sent': np.random.uniform(15000, 50000, sub_size), # High outgoing data
    'bytes_received': np.random.uniform(100, 800, sub_size),
    'login_attempts': np.ones(sub_size), # This looks "normal" to a dumb AI!
    'label': 1 
}

# Combine all three types into one table
df_normal = pd.DataFrame(normal_traffic)
df_brute = pd.DataFrame(brute_force)
df_exfil = pd.DataFrame(data_exfiltration)

df = pd.concat([df_normal, df_brute, df_exfil]).sample(frac=1).reset_index(drop=True)

# Save to the data folder
df.to_csv('data/network_traffic.csv', index=False)

print(f"Success! Created {len(df)} rows of diverse traffic data.")
print("The AI will now learn to catch 'The Thief' even if login attempts are 1.")