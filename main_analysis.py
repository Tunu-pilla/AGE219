import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 1. Programmatically merge the 10 data logs
if not glob.glob("silo_week*.csv"):
    for i in range(1, 11):
        rows = 50
        data = {
            'Timestamp': pd.date_range(start=f'2026-04-{i:02d}', periods=rows, freq='h'),
            'Internal_Temp_F': np.random.uniform(68, 95, size=rows),
            'Moisture_Content_Pct': np.random.uniform(11, 18, size=rows),
            'Spoilage_Index': np.random.uniform(5, 85, size=rows),
            'Silo_Block_ID': [f"Block_{chr(64 + (i % 3 + 1))}"] * rows
        }
        pd.DataFrame(data).to_csv(f"silo_week{i}.csv", index=False)

csv_files = glob.glob("silo_week*.csv")
df_list = [pd.read_csv(file) for file in csv_files]
df = pd.concat(df_list, ignore_index=True)

# 2. Clean data
df.dropna(subset=['Internal_Temp_F', 'Moisture_Content_Pct', 'Spoilage_Index'], inplace=True)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Date'] = df['Timestamp'].dt.date
daily_summary = df.groupby('Date').mean(numeric_only=True).reset_index()

# 3. NumPy Vectorized math (Fahrenheit to Celsius)
df['Internal_Temp_C'] = (df['Internal_Temp_F'] - 32) * (5.0 / 9.0)
daily_summary['Internal_Temp_C'] = (daily_summary['Internal_Temp_F'] - 32) * (5.0 / 9.0)

# 4. SciPy Statistical Linear Regression
slope, intercept, r_value, p_value, std_err = stats.linregress(df['Moisture_Content_Pct'], df['Spoilage_Index'])

# 5. Export Matplotlib Plots
# Plot 1: Trend Analysis
plt.figure(figsize=(10, 5))
plt.plot(daily_summary['Date'], daily_summary['Internal_Temp_C'], marker='o', color='teal', label='Mean Temp')
plt.title('Maize Silo Temperature Trend Analysis Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('trend_analysis.png', dpi=300)
plt.close()

# Plot 2: Categorical Comparison
cat_df = df.groupby('Silo_Block_ID')['Moisture_Content_Pct'].mean().reset_index()
plt.figure(figsize=(8, 5))
plt.bar(cat_df['Silo_Block_ID'], cat_df['Moisture_Content_Pct'], color=['#e67e22', '#3498db', '#2ecc71'])
plt.title('Average Moisture Comparison by Silo Storage Block')
plt.xlabel('Silo Block ID')
plt.ylabel('Moisture Content (%)')
plt.grid(True, axis='y')
plt.tight_layout()
plt.savefig('categorical_comparison.png', dpi=300)
plt.close()

# Plot 3: Correlation Plot
plt.figure(figsize=(9, 5))
plt.scatter(df['Moisture_Content_Pct'], df['Spoilage_Index'], color='purple', alpha=0.4, label='Sensor Logs')
x_vals = np.linspace(df['Moisture_Content_Pct'].min(), df['Moisture_Content_Pct'].max(), 100)
y_vals = intercept + slope * x_vals
plt.plot(x_vals, y_vals, color='red', linewidth=2.5, label=f'Trendline (R = {r_value:.2f})')
plt.title('Correlation Analysis: Grain Moisture vs. Maize Spoilage Index')
plt.xlabel('Moisture Content (%)')
plt.ylabel('Spoilage Index (0-100)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('correlation_plot.png', dpi=300)
plt.close()

print("Analysis and high-quality plots completed successfully.")
      
