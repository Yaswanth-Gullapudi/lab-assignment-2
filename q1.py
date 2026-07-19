import pandas as pd
import numpy as np

# Load data
df = pd.read_excel("C:/Users/yashu/Downloads/Lab Session Data.xlsx",sheet_name="Purchase data")
# Create matrices
X = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]].to_numpy()
y = df[["Payment (Rs)"]].to_numpy()

# Basic information
print("Dimensionality:", X.shape[1])
print("Number of vectors:", X.shape[0])

# Rank
rank_X = np.linalg.matrix_rank(X)
print("Rank of X:", rank_X)

# Pseudo-inverse and product costs
c = np.linalg.pinv(X) @ y

print("\nEstimated Costs:")
print(f"Candies (Rs): {c[0,0]}")
print(f"Mangoes (Rs/kg): {c[1,0]}")
print(f"Milk Packets (Rs): {c[2,0]}")