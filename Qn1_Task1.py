import pandas as pd

# Define the paths to CSV files and their corresponding text columns
file_info = [
    {'path': 'C:/Users/subed/OneDrive/Desktop/softassign/CSV1.csv', 'text_column': 'SHORT-TEXT'},
    {'path': 'C:/Users/subed/OneDrive/Desktop/softassign/CSV2.csv', 'text_column': 'TEXT'},
    {'path': 'C:/Users/subed/OneDrive/Desktop/softassign/CSV3.csv', 'text_column': 'TEXT'},
    {'path': 'C:/Users/subed/OneDrive/Desktop/softassign/CSV4.csv', 'text_column': 'TEXT'}
]

# Function to extract text from CSV files
def extract_text_from_csvs(file_info):
    text_data = []
    
    for file in file_info:
        file_path = file['path']
        text_column_name = file['text_column']
        try:
            df = pd.read_csv(file_path)
            if text_column_name in df.columns:
                text_data.extend(df[text_column_name].dropna().tolist())  # Extract non-null text data
            else:
                print(f"'{text_column_name}' column not found in {file_path}")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    return text_data

# Function to write text data to a single .txt file
def write_to_text_file(text_data, output_file='combined_texts.txt'):
    with open(output_file, 'w', encoding='utf-8') as f:
        for text in text_data:
            f.write(text + '\n')

# Extract text and write to a .txt file
text_data = extract_text_from_csvs(file_info)
write_to_text_file(text_data, 'combined_texts.txt')

print(f"Text data successfully written to combined_texts.txt")
