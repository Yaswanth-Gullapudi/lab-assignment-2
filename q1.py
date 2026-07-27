import pandas as pd
import numpy as np

df = pd.read_excel("C:/Users/yashu/Downloads/Lab Session Data.xlsx",sheet_name="Purchase data")
X = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]].to_numpy()
y = df[["Payment (Rs)"]].to_numpy()

print("Dimensionality:", X.shape[1])
print("Number of vectors:", X.shape[0])

rank_X = np.linalg.matrix_rank(X)
print("Rank of X:", rank_X)

c = np.linalg.pinv(X) @ y

print("\nEstimated Costs:")
print(f"Candies (Rs): {c[0,0]}")
print(f"Mangoes (Rs/kg): {c[1,0]}")
print(f"Milk Packets (Rs): {c[2,0]}")
