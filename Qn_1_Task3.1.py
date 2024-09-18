import re
from collections import Counter
import pandas as pd

# Function to count the top 30 most common words in a text file
def count_words_in_text(file_path, output_csv='top_30_common_words.csv'):
    # Read the .txt file
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()  # Convert text to lowercase
    
    # Remove punctuation and non-alphabetic characters
    words = re.findall(r'\b\w+\b', text)
    
    # Count occurrences of each word
    word_counts = Counter(words)
    
    # Get the top 30 most common words
    top_30_words = word_counts.most_common(30)
    
    # Convert to a DataFrame
    df = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
    
    # Save the top 30 words and their counts to a CSV file
    df.to_csv(output_csv, index=False)
    print(f"Top 30 words and their counts saved to {output_csv}")

# Example usage
count_words_in_text('combined_texts.txt')

