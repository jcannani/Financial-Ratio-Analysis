import pandas as pd
# Load the CSV file
df = pd.read_csv("./balance_sheet.csv")

# Check Raw Data
print("Raw Data:")
print(df)

# Print cleaned Data
print("\nCleaned Data:")
print(df)

# Print Data Types
print("\nData Types:")
print(df.dtypes)

# Clean and convert currency columns to float, if needed
df.columns = df.columns.str.strip()
columns_to_convert = ['Current Assets:','Total Assets:','Current Liabilities:','Total Liabilities:','Total Equity:']
for col in columns_to_convert:
    #Remove dollar signs and commas, then convert to float
    df[col] = df[col].replace(r'[\$,]','', regex=True)
    df[col] = pd.to_numeric(df[col], errors='coerce') # Convert to float, set bad values to NaN
print(df.dtypes)

# Calculate Financial Ratios
df['Current Ratio'] = df['Current Assets:'] / df['Current Liabilities:']
df['Debt-to-Equity'] = df['Total Liabilities:'] / df['Total Equity:']
df['Equity Ratio'] = df['Total Equity:'] / df['Total Assets:']
df['Working Capital'] = df['Current Assets:'] - df['Current Liabilities:']
df['Debt Ratio'] = df['Total Liabilities:'] - df['Total Assets:']

# Optional: Round results for neat output
df = df.round(2)

# Show the results
print("\nCalculated Financial Ratios:")
print(df[['Year:','Current Ratio','Debt-to-Equity','Equity Ratio','Working Capital','Debt Ratio']])

import matplotlib.pyplot as plt

# Visualizing financial ratio trends
plt.figure(figsize=(12, 6))

# Line chart of multiple ratios
plt.plot(df['Year:'], df['Current Ratio'], marker='o', label='Current Ratio')
plt.plot(df['Year:'], df['Debt-to-Equity'], marker='o', label='Debt-to-Equity')
plt.plot(df['Year:'], df['Equity Ratio'], marker='o', label='Equity Ratio')

# Customize the chart
plt.title('Year-over-Year Financial Ratios')
plt.xlabel('Year')
plt.ylabel('Ratio Value')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Display the chart
plt.show()
