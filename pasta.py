import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats

df = pd.read_excel("pasta.xlsx")
sns.distplot(df["len"])
d = df["len"]
print(stats.kstest(d, 'norm', (d.mean(), d.std()), N=100))
#plt.plot([1,2,3], [3,4,5])
plt.show()
#print(df)
