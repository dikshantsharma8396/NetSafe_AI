import joblib
import pandas as pd

# 1. Load the "Brain" we saved earlier
model = joblib.load('models/netsafe_model.pkl')

def check_traffic(duration, bytes_sent, bytes_received, login_attempts):
    # 2. Put the new data into a format the AI understands (a DataFrame)
    new_data = pd.DataFrame({
        'duration': [duration],
        'bytes_sent': [bytes_sent],
        'bytes_received': [bytes_received],
        'login_attempts': [login_attempts]
    })
    
    # 3. Ask the AI for its opinion
    prediction = model.predict(new_data)
    
    # 4. Translate the 0 or 1 into human language
    if prediction[0] == 0:
        return "✅ NORMAL: Everything looks safe."
    else:
        return "🚨 ALERT: Potential Attack Detected!"

# --- TEST SCENARIOS ---

print("--- NetSafe_AI Live Scanner Test ---")

# Scenario A: A normal user checking a website
print("\nTesting Scenario A (Normal User):")
print(check_traffic(duration=2, bytes_sent=200, bytes_received=300, login_attempts=1))

# Scenario B: A hacker trying to brute force a password
print("\nTesting Scenario B (Hacker Attack):")
print(check_traffic(duration=150, bytes_sent=15000, bytes_received=12000, login_attempts=15))