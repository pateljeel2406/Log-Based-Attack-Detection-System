import pandas as pd
from sklearn.ensemble import IsolationForest

print("MACHINE LEARNING ATTACK DETECTION")
print("--------------------------------")

# Login data
data = {
    "Failed_Attempts": [0, 1, 0, 2, 1, 10, 12, 15, 0, 3]
}

df = pd.DataFrame(data)

# Machine Learning Model
model = IsolationForest(
    contamination=0.2,
    random_state=42
)

model.fit(df)

# Detect suspicious activity
df["Result"] = model.predict(df[["Failed_Attempts"]])

print("\nLogin Analysis:\n")

for index, row in df.iterrows():
    if row["Result"] == -1:
        print(row["Failed_Attempts"], "Failed Attempts - SUSPICIOUS!")
    else:
        print(row["Failed_Attempts"], "Failed Attempts - Normal")

print("\nMACHINE LEARNING SCAN COMPLETED")