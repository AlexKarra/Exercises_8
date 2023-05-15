# 1
def write_to_file(text, output_file_path):
    import os
    if os.path.exists(output_file_path):
        raise RuntimeError("Output file already exists!")
    with open(output_file_path, "w") as f:
        f.write(text)
        
text = "Hi, my name is Alex!"
output_file_path = "output.txt"

try:
    write_to_file(text, output_file_path)
    print(f"Successfully wrote '{text}' to '{output_file_path}'.")
except RuntimeError as e:
    print(f"Error: {e}")
    
    
# 2

import spacy

def count_stopwords(input_file_path):
  # Loading the English language model
    nlp = spacy.load("en_core_web_sm")

  # Loading the text from the input file
  with open(input_file_path) as f:
        text = f.read()

  # Parsing the text with spaCy
  doc = nlp(text)

  # Counting the number of stopwords in the document
  num_stopwords = len([token for token in doc if token.is_stop])

  return num_stopwords


# 3

(import spacy)

def remove_stopwords(input_file_path, output_file_path):
    nlp = spacy.load("en_core_web_sm")

    with open(input_file_path) as f:
        text = f.read()
        
    doc = nlp(text)

    # Removing stopwords from the document and joining the remaining tokens
    filtered_text = " ".join([token.text for token in doc if not token.is_stop])

    # Writing the filtered text to the output file
    with open(output_file_path, "w") as f:
        f.write(filtered_text)
        
        
# 4

(import spacy)

def tokenize_text(input_file_path, output_file_path):
    nlp = spacy.load("en_core_web_sm")

    with open(input_file_path, "r") as input_file:
        text = input_file.read()

    # Tokenizing the text using spaCy
    doc = nlp(text)

    # Writing the tokens to the output file in a tabular form
    with open(output_file_path, "w") as output_file:
        output_file.write("Token\tLemma\tPOS\n")
        for token in doc:
            output_file.write(f"{token.text}\t{token.lemma_}\t{token.pos_}\n")
            
            
# 5

(import spacy)
from spacy import displacy

def save_visualization(input_file_path, output_file_path):
    nlp = spacy.load('en_core_web_sm')

    with open(input_file_path, 'r') as input_file:
        text = input_file.read()

    # Creating a Doc object from the text using spaCy
    doc = nlp(text)

    # Visualizing the dependencies of the tokens using displacy
    svg = displacy.render(doc, style='dep', jupyter=False)

    # Saving the visualization as an .svg file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(svg)
        
input_file_path = 'input.txt'
output_file_path = 'output.svg'
save_visualization(input_file_path, output_file_path)
