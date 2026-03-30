import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# 1. Load the data we generated
print("Step 2: Loading the 'textbook' (data)...")
df = pd.read_csv('data/network_traffic.csv')

# 2. Separate the "Questions" (Features) from the "Answers" (Labels)
# X = the data (duration, bytes, etc.)
# y = the answer (0 for normal, 1 for attack)
X = df.drop('label', axis=1)
y = df['label']

# 3. Split into "Study Material" and "Exam"
# We use 80% to train the AI and 20% to test if it actually learned
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize the "Student" (Random Forest Model)
print("Step 3: Training the AI 'Brain'...")
model = RandomForestClassifier(n_estimators=100)

# 5. The actual "Learning" process
model.fit(X_train, y_train)

# 6. Take the "Exam" (Test the accuracy)
predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)

print(f"Success! The AI finished its exam with an accuracy of: {score * 100}%")

# 7. Save the "Brain" so we can use it later without re-training
if not os.path.exists('models'):
    os.makedirs('models')
    
joblib.dump(model, 'models/netsafe_model.pkl')
print("The trained model has been saved in 'models/netsafe_model.pkl'")