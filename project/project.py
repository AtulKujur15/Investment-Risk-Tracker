import pandas as pd
import datetime as dt
df=pd.read_csv("NIFTY 50.csv")
df['Year'] = pd.DatetimeIndex(df['Date']).year

new_df=(df.groupby('Year').first())
new_df['Return']=((50000/new_df['Open'])*new_df['Open'].iloc[-1])
print(new_df)
inv=new_df['Return'].sum()
print((inv-1100000)/1100000*100)



