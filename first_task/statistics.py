import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()

df = pd.read_csv('extensions.csv')
sns.scatterplot(x='Num ratings',y = 'Users', hue = 'Rank',data = df)
plt.show()