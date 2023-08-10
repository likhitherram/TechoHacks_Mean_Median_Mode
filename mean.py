import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data= pd.read_csv(r"C:\Users\LIKHITH\Desktop\python_ws\train.csv")

data

data.describe()

data.mean(numeric_only=True)

data.median(numeric_only=True)

data.mode()

data.std(numeric_only=True)
