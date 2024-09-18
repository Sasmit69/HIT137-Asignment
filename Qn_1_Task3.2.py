import warnings
from transformers import AutoTokenizer
from collections import Counter
import pandas as pd

# Suppress the specific warning
warnings.filterwarnings("ignore", message=".*clean_up_tokenization_spaces.*")

# Function to count unique tokens
def count_unique_tokens(file_path, model_name='bert-base-uncased', output_csv='top_30_tokens.csv'):
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Read the text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Check if the file was read correctly
    if not text:
        print("Error: File is empty or not readable.")
        return

    print("File read successfully. Tokenizing...")

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Check if tokenization was successful
    if not tokens:
        print("Error: No tokens were generated.")
        return

    # Print the first 100 tokens for debugging purposes
    print(f"First 100 tokens: {tokens[:100]}")

    # Count token occurrences
    token_counts = Counter(tokens)
    
    # Check how many unique tokens are there
    print(f"Total unique tokens: {len(token_counts)}")

    # Get the top 30 most common tokens
    top_30_tokens = token_counts.most_common(30)

    # Check if there are fewer than 30 tokens
    if len(top_30_tokens) < 30:
        print(f"Warning: Only found {len(top_30_tokens)} unique tokens.")

    # Convert to a DataFrame and save to a CSV file
    df = pd.DataFrame(top_30_tokens, columns=['Token', 'Count'])
    df.to_csv(output_csv, index=False)

    print(f"Top {len(top_30_tokens)} tokens saved to {output_csv}")

# Usage example
count_unique_tokens('combined_texts.txt')
