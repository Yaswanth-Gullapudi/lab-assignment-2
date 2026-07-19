import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

file = r"C:/Users/yashu/Downloads/Lab Session Data.xlsx"
df = pd.read_excel(file, sheet_name="IRCTC Stock Price")

df["Date"] = pd.to_datetime(df["Date"])
df["Day"] = df["Date"].dt.day_name()

price = df["Price"].dropna().to_numpy()

mean_np = np.mean(price)
var_np = np.var(price)

def my_mean(x):
    s = 0
    for v in x:
        s += v
    return s / len(x)

def my_var(x):
    m = my_mean(x)
    s = 0
    for v in x:
        s += (v - m) ** 2
    return s / len(x)

mean_my = my_mean(price)
var_my = my_var(price)

def avg_time(func, data, runs=10):
    t = []
    for _ in range(runs):
        st = time.perf_counter()
        func(data)
        et = time.perf_counter()
        t.append(et - st)
    return np.mean(t)

t_np_mean = avg_time(np.mean, price)
t_my_mean = avg_time(my_mean, price)
t_np_var = avg_time(np.var, price)
t_my_var = avg_time(my_var, price)

wed_mean = df[df["Day"] == "Wednesday"]["Price"].mean()

apr_mean = df[df["Date"].dt.month == 4]["Price"].mean()

df["Chg%"] = df["Chg%"].astype(str).str.replace("%", "", regex=False).astype(float)

prob_loss = (df["Chg%"] < 0).mean()

wed = df[df["Day"] == "Wednesday"]
prob_profit_wed = (wed["Chg%"] > 0).mean()

print("Mean:", mean_np)
print("Var :", var_np)
print("My Mean:", mean_my)
print("My Var :", var_my)
print("dMean:", abs(mean_np - mean_my))
print("dVar :", abs(var_np - var_my))
print("T np mean:", t_np_mean)
print("T my mean:", t_my_mean)
print("T np var :", t_np_var)
print("T my var :", t_my_var)
print("Wed Mean:", wed_mean)
print("Apr Mean:", apr_mean)
print("P(Loss):", prob_loss)
print("P(Profit|Wed):", prob_profit_wed)

plt.scatter(df["Day"], df["Chg%"])
plt.xlabel("Day")
plt.ylabel("Chg%")
plt.show()