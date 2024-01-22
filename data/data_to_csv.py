import pandas as pd

data = pd.io.stata.read_stata('2021trade4digit.dta')
data.to_csv('2021trade4digit.csv')