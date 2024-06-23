import time
import pandas as pd

tic1 = time.perf_counter()
df = pd.read_csv("loan_data.csv")
toc1 = time.perf_counter()

tic2 = time.perf_counter()
datax = df['grade'].value_counts().sort_index()

datay = pd.DataFrame({
    'Grade': datax.index,
    'Frequency': datax.values,
    'Percent': ((datax.values / datax.values.sum()) * 100).round(2),
    'Cumulative Frequency': datax.values.cumsum(),
    'Cumulative Percent': ((datax.values.cumsum() / datax.values.sum()) * 100).round(2)
})
print(datay)
toc2 = time.perf_counter()

tic3 = time.perf_counter()
datax = df['grade'].value_counts()
datay = pd.DataFrame({
    'Grade': datax.index,
    'Frequency': datax.values,
    'Percent': ((datax.values / datax.values.sum()) * 100).round(2),
    'Cumulative Frequency': datax.values.cumsum(),
    'Cumulative Percent': ((datax.values.cumsum() / datax.values.sum()) * 100).round(2)
})
print(datay)
toc3 = time.perf_counter()

tic4 = time.perf_counter()
datax = df['grade'].value_counts().sort_index()

datay = pd.DataFrame({
    'grade': datax.index,
    'Frequency': datax.values
})
print(datay)
toc4 = time.perf_counter()

tic5 = time.perf_counter()
datab = pd.crosstab(df.grade, df.grade_cat, margins=True, margins_name="Total")
print(datab)
toc5 = time.perf_counter()

print(f"Loaded data in {toc1 - tic1:0.9f} seconds.")
print(f"run basic proc freq table in {toc2 - tic2:0.4f} seconds.")
print(f"run proc freq table sorted by frequency in {toc3 - tic3:0.4f} seconds.")
print(f"run proc freq table norow nocol nopercentage in {toc4 - tic4:0.4f} seconds.")
print(f"run proc freq table crosstab in {toc5 - tic5:0.4f} seconds.")

print(df.shape)