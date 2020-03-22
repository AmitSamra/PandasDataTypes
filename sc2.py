import pandas as pd
import numpy as np

df = pd.read_csv("https://github.com/chris1610/pbpython/blob/master/data/sales_data_types.csv?raw=True")

#print(df)

df['Customer Number'] = df['Customer Number'].astype('int')

def convert_currency(val):
    new_val = val.replace(',','').replace('$','')
    return float(new_val)

def convert_percent(val):
    new_val = val.replace('%','')
    return float(new_val)/100

df['2016'] = df['2016'].apply(convert_currency)
df['2017'] = df['2017'].apply(convert_currency)
df['Percent Growth'] = df['Percent Growth'].apply(convert_percent)

df["Jan Units"] = pd.to_numeric(df['Jan Units'], errors='coerce').fillna(0)

df['Start Date'] = pd.to_datetime(df[ ['Month', 'Day', 'Year'] ])

df['Active'] = np.where(df['Active'] == 'Y', True, False)

print(df)
