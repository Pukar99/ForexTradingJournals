import pandas as pd

# Read the CSV file
df = pd.read_csv("trading_journal_demo_data.csv")

# Generate descriptive statistics
descriptive_stats = df.describe(include='all')

# Create an MD file and write the statistics
with open("trading_journal_statistics.md", "w") as f:
    f.write("# Trading Journal Descriptive Statistics\n\n")
    f.write(descriptive_stats.to_markdown())
