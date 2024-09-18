import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import pandas as pd

# Load the SpaCy models for medical NER (Named Entity Recognition)
nlp_sci_sm = spacy.load("en_core_sci_sm")  # A general medical model
nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")  # Specialized model for diseases and chemicals (drugs)

# Load BioBERT model using Hugging Face
tokenizer_biobert = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
model_biobert = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
biobert_ner = pipeline("ner", model=model_biobert, tokenizer=tokenizer_biobert)

# Function to read the text from the .txt file
def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

# Function to extract entities using SpaCy
def extract_entities_spacy(text, model, entity_label):
    doc = model(text)
    entities = [ent.text for ent in doc.ents if ent.label_ == entity_label]
    return entities

# Function to extract entities using BioBERT
def extract_entities_biobert(text):
    ner_results = biobert_ner(text)
    diseases = [entity['word'] for entity in ner_results if 'disease' in entity['entity'].lower()]
    drugs = [entity['word'] for entity in ner_results if 'drug' in entity['entity'].lower()]
    return diseases, drugs

# Read the text file (change 'combined_texts.txt' to your file path if needed)
text = read_text_file('combined_texts.txt')

if text:
    # Extract diseases and drugs using the SpaCy models
    diseases_bc5cdr = extract_entities_spacy(text, nlp_bc5cdr, 'DISEASE')
    drugs_bc5cdr = extract_entities_spacy(text, nlp_bc5cdr, 'CHEMICAL')

    # Extract diseases and drugs using BioBERT
    diseases_biobert, drugs_biobert = extract_entities_biobert(text)

    # Compare the results: find common and unique entities between the two models
    def compare_entities(entities1, entities2, label):
        common = set(entities1).intersection(set(entities2))  # Entities found by both models
        unique_1 = set(entities1) - common  # Entities found only by Model 1
        unique_2 = set(entities2) - common  # Entities found only by Model 2

        print(f"\nComparison for {label}:")
        print(f"Total detected by Model 1 (SpaCy): {len(entities1)}")
        print(f"Total detected by Model 2 (BioBERT): {len(entities2)}")
        print(f"Common {label}: {len(common)}")
        print(f"Unique to Model 1: {len(unique_1)}")
        print(f"Unique to Model 2: {len(unique_2)}")

        return common, unique_1, unique_2

    # Compare diseases
    common_diseases, unique_bc5cdr_diseases, unique_biobert_diseases = compare_entities(diseases_bc5cdr, diseases_biobert, "diseases")

    # Compare drugs
    common_drugs, unique_bc5cdr_drugs, unique_biobert_drugs = compare_entities(drugs_bc5cdr, drugs_biobert, "drugs")

    # Save the comparison results to a CSV file
    def save_comparison_to_csv(common, unique1, unique2, label):
        df = pd.DataFrame({
            f'Common {label}': list(common),
            f'Unique to Model 1 (SpaCy)': list(unique1),
            f'Unique to Model 2 (BioBERT)': list(unique2)
        })
        output_file = f'comparison_{label.lower()}.csv'
        df.to_csv(output_file, index=False)
        print(f"Comparison results saved to {output_file}")

    # Save comparison results for diseases and drugs to CSV files
    save_comparison_to_csv(common_diseases, unique_bc5cdr_diseases, unique_biobert_diseases, 'diseases')
    save_comparison_to_csv(common_drugs, unique_bc5cdr_drugs, unique_biobert_drugs, 'drugs')
