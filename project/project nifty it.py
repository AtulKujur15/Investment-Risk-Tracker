import pandas as pd
import os
from matplotlib import pyplot as plt


path = r"C:\Users\Admin\Desktop\codersdaily\project\Collection"


files = os.listdir(path)
print(files)

returns_list = []
file_names = []

for file in files:
    try:
        full_path = os.path.join(path, file)
        df = pd.read_csv(full_path)

        
        df.columns = df.columns.str.strip()

        
        if 'Date' not in df.columns or 'Open' not in df.columns:
            print(file, "Missing required columns")
            continue

        
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df.dropna(subset=['Date'], inplace=True)

        
        df['Year'] = df['Date'].dt.year

        
        yearly_data = df.groupby('Year').first().dropna()

        number_of_years = len(yearly_data)
        total_investment = 50000 * number_of_years

        
        yearly_data['Return'] = (
            (50000 / yearly_data['Open']) * yearly_data['Open'].iloc[-1]
        )

        total_value = yearly_data['Return'].sum()
        percent_return = ((total_value - total_investment) / total_investment) * 100

        file_names.append(file)
        returns_list.append(percent_return)

    except Exception as e:
        print(file, "Error:", e)

print("Processed files:", len(file_names))
print("Return values:", len(returns_list))


plt.figure(figsize=(12, 6))
plt.bar(file_names, returns_list)
plt.xticks(rotation=90)
plt.title("Yearly Investment Return Comparison")
plt.tight_layout()
plt.show()
