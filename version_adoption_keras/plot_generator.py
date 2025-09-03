import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
file_path = 'bquxjob_7e772f9e_1985d03a1ba.csv'
df = pd.read_csv(file_path)

# Filter out versions below a threshold
threshold = 500_000
df = df[df['download_count'] >= threshold]

# Sort by download count descending
df = df.sort_values(by='download_count', ascending=False)

# Plotting
plt.figure(figsize=(14, 6))
bars = plt.bar(df['version'], df['download_count'], color='#D25D5D')

# Add formatted text annotations above bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height // 2,
             f'{height/1_000_000:.1f}M',
             ha='center', va='top', fontsize=28)

plt.xlabel('Version (x.y.z)', fontsize=30)
plt.ylabel('Download Counts', fontsize=30)
plt.xticks(rotation=0, fontsize=28)  # X-axis tick labels
plt.yticks([], fontsize=28)          # Hide Y-axis tick labels
plt.tight_layout()
plt.show()