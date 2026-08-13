import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns

def c_mean(arr):
    t = sum(arr)
    return t / len(arr)

def c_var(arr):
    a = c_mean(arr)
    v = sum((x - a) ** 2 for x in arr)
    return v / len(arr)

if __name__ == "__main__":
    f = r"C:\Users\yashu\Downloads\Lab Session Data.xlsx"
    df = pd.read_excel(f, sheet_name='IRCTC Stock Price')
    p = df['Price'].values

    t0 = time.time()
    for _ in range(10):
        c_mean(p)
        c_var(p)
    t_c = (time.time() - t0) / 10

    t0 = time.time()
    for _ in range(10):
        np.mean(p)
        np.var(p)
    t_n = (time.time() - t0) / 10

    print("custom time:", t_c)
    print("numpy time:", t_n)

    w_m = np.mean(df[df['Day'] == 'Wed']['Price'])
    a_m = np.mean(df[df['Month'] == 'Apr']['Price'])
    print("wed mean:", w_m)
    print("apr mean:", a_m)

    chg = df['Chg%'].values
    loss = list(filter(lambda x: x < 0, chg))
    p_l = len(loss) / len(chg)
    
    wed = df[df['Day'] == 'Wed']
    p_p_w = len(wed[wed['Chg%'] > 0]) / len(df)
    c_p = len(wed[wed['Chg%'] > 0]) / len(wed)

    print("prob loss:", p_l)
    print("prob profit and wed:", p_p_w)
    print("prob profit given wed:", c_p)

    sns.scatterplot(data=df, x='Day', y='Chg%')
    plt.show()