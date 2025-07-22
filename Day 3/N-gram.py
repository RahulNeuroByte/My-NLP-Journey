def generate_ngrams(text, n):
    # step:1 Preprocess the text

    tokens = text.lower().split()

    # step:2 Create the n- gram
    ngrams = []
    for i in range (len(tokens) - n +1):
        ngram = tuple(tokens[i:i + n])
        ngrams.append(ngram)

    return ngrams


# Example usage

if __name__ == "__main__":
    text = "I love natural language processing"
    n = int(input("Enter the value of n:"))
    # 1 for unigrams, 2 for bigrams, 3 for trigrams, etc.

    result = generate_ngrams(text,n)

    print(f"{n}-grams:")

    for gram in result:
        print(gram)
    
