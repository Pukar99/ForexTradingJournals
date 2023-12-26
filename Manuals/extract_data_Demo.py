
#after the completion of a month/ completing entries this code is used to extract the files datas  attribute to csv file which further used for data analaysis.

import os
import pandas as pd
import markdown
from bs4 import BeautifulSoup

# Function to extract information from a Markdown file
def extract_info_from_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(markdown.markdown(content), 'html.parser')

        # Extract information from the HTML content (modify this based on your file structure)
        strategy = soup.find('h1').text.strip()
        instrument = soup.find('strong', text='Instrument:').next_sibling.strip()
        position_size = soup.find('strong', text='Position Size:').next_sibling.strip()
        risk_reward_ratio = soup.find('strong', text='Risk-Reward Ratio:').next_sibling.strip()
        entry_price = soup.find('strong', text='Entry Price:').next_sibling.strip()
        confidence_level = soup.find('strong', text='Confidence Level:').next_sibling.strip()
        result = soup.find('strong', text='Result:').next_sibling.strip()
        profit_loss = soup.find('strong', text='Profit/Loss:').next_sibling.strip()

        return {
            'Strategy': strategy,
            'Instrument': instrument,
            'Position Size': position_size,
            'Risk-Reward Ratio': risk_reward_ratio,
            'Entry Price': entry_price,
            'Confidence Level': confidence_level,
            'Result': result,
            'Profit/Loss': profit_loss,
        }

# Directory containing Markdown files
demo_directory = '2023/Demo'

# List to store extracted information from each file
entries_data = []

# Loop through each file in the directory
for file_name in os.listdir(demo_directory):
    if file_name.endswith('.md'):
        file_path = os.path.join(demo_directory, file_name)
        entry_data = extract_info_from_md(file_path)
        entries_data.append(entry_data)

# Create a DataFrame
df = pd.DataFrame(entries_data)

# Define the file path for CSV export
csv_file_path = 'trading_journal_demo_data.csv'

# Export DataFrame to CSV
df.to_csv(csv_file_path, index=False)

# Display the DataFrame
print(df)
