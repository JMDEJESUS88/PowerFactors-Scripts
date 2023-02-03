import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a Pandas DataFrame --- edit file path as needed
df = pd.read_excel(r'C:\Users\JeremiahDeJesus\Documents\GitHub\data-graph\Foton.xlsx')

# Convert the timestamp column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')

# Set the timestamp column as the index
df = df.set_index('timestamp')

# Plot a separate graph for each tag and save it as a PNG file
for tag in df['tags'].unique():
    tag_df = df[df['tags'] == tag]
    plt.figure(figsize=(20, 10))
    plt.step(tag_df.index, tag_df['value'], label=tag)
    plt.title(f'Graph for tag: {tag}')
    plt.legend()
    plt.xticks(rotation=90)
    plt.savefig(f'{tag}.png')

# Show the graph
#plt.show()
