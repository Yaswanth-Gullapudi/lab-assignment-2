import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_jc_smc(v1, v2):
    f11 = np.sum((v1 == 1) & (v2 == 1))
    f00 = np.sum((v1 == 0) & (v2 == 0))
    f10 = np.sum((v1 == 1) & (v2 == 0))
    f01 = np.sum((v1 == 0) & (v2 == 1))
    
    d_j = f11 + f10 + f01
    jc = f11 / d_j if d_j > 0 else 0
    
    d_s = f11 + f00 + f10 + f01
    smc = (f11 + f00) / d_s if d_s > 0 else 0
    return jc, smc

def get_cos(v1, v2):
    n = (np.linalg.norm(v1) * np.linalg.norm(v2))
    if n == 0: return 0
    return np.dot(v1, v2) / n

if __name__ == "__main__":
    f = r"C:\Users\yashu\Downloads\Lab Session Data.xlsx"
    df = pd.read_excel(f, sheet_name='thyroid0387_UCI').replace('?', np.nan)
    top = df.head(20).copy()
    
    b_cols = [c for c in top.columns if set(top[c].dropna().unique()).issubset({'t', 'f', 'F', 'M'})]
    b_df = top[b_cols].copy().replace({'t': 1, 'M': 1, 'f': 0, 'F': 0})
    b_mat = b_df.values
    
    n_df = top.drop(columns=['Record ID', 'referral source', 'Condition']).replace({'t': 1, 'M': 1, 'f': 0, 'F': 0})
    n_mat = n_df.apply(pd.to_numeric, errors='coerce').fillna(0).values

    jc, smc = get_jc_smc(b_mat[0], b_mat[1])
    cos = get_cos(n_mat[0], n_mat[1])
    
    print("vec 1 and 2 jc:", jc)
    print("vec 1 and 2 smc:", smc)
    print("vec 1 and 2 cos:", cos)

    n = b_mat.shape[0]
    j_m = np.zeros((n, n))
    s_m = np.zeros((n, n))
    c_m = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            j_m[i, j], s_m[i, j] = get_jc_smc(b_mat[i], b_mat[j])
            c_m[i, j] = get_cos(n_mat[i], n_mat[j])

    fig, ax = plt.subplots(1, 3, figsize=(15, 4))
    sns.heatmap(j_m, ax=ax[0])
    sns.heatmap(s_m, ax=ax[1])
    sns.heatmap(c_m, ax=ax[2])
    plt.show()