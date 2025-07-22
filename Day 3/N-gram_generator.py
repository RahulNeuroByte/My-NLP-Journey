import re
from collections import Counter 

def clean_text(text):
    text  = text.lower()
    text = re.sub('[^a-z\s]', ' ',text) # Remove punctuation and special characters
    text = re.sub(r'\s+', ' ',text).strip() # Remove extra spaces
    return text 

def generate_ngrams(tokens,n):

    # generate n-grams from token list
    ngrams = []
    for i in range(len(tokens) -n + 1):
        ngram = tuple(tokens[i:i + n])
        ngrams.append(ngram)
    return ngrams


def display_ngrams(ngrams):
    # display each n-gram and its frequency
    print("\n Generated N-grams:\n")
    for gram in ngrams:
        print(gram)

    freq =Counter(ngrams)
    print("\n Frequency of each N-gram:\n")
    for k, v in freq.items():
        print(f"{k}: {v}")

def main():
    print("Welcome to the Custom N-gram Generator")


    # step1: Get user input ...can pass multiline text
    print("Enter your text:")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    full_text = " ".join(lines)

    if not full_text.strip():
        print("no text provided")
        return
    
    # step2: Clean the text and tokenize
    cleaned_text = clean_text(full_text)
    tokens = cleaned_text.split()

    if len(tokens) < 1:
        print("Not enough words to process.")
        return
    
    # step3: Take n value from user

    try:
        n = int(input("Enter the value of n (1 for unigrams, 2 for bigrams and 3 for trigrams)"))
    except ValueError:
        print("Please enter a valid integer for n.")
        return
    
    if n <= 0 or n > len(tokens):
        print("Invalid value for n.")
        return
    
    # step4: Generate and display
    ngrams = generate_ngrams(tokens,n)
    display_ngrams(ngrams)

if __name__ == "__main__":
    main()
