from nltk.corpus import wordnet as wn

# Step 1: Load WordNet
def load_wordnet():
    wordnet_dict = {}
    for synset in wn.all_synsets():
        for lemma in synset.lemmas():
            word = lemma.name().lower()
            description = synset.definition()
            classification = synset.pos()
            if word not in wordnet_dict:
                wordnet_dict[word] = (description, classification)
    return wordnet_dict

# Step 3: Validation function with description and classification
def validate_word(word, wordnet_dict):
    word = word.lower()
    if word in wordnet_dict:
        return True, wordnet_dict[word]
    else:
        return False, None

# Step 5: Feedback function with description and classification
def provide_feedback(word, is_valid, description=None, classification=None):
    if is_valid:
        print(f"The word '{word}' is valid!")
        if description and classification:
            print(f"Description: {description}\nClassification: {classification}")
    else:
        print(f"Sorry, '{word}' is not a valid word.")

# Step 2 & 4: User input and integration
def main():
    wordnet_dict = load_wordnet()
    while True:
        user_input = input("Enter a word to validate \n(or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        is_valid, word_info = validate_word(user_input, wordnet_dict)
        if is_valid:
            description, classification = word_info
        else:
            description, classification = None, None
        provide_feedback(user_input, is_valid, description, classification)

if __name__ == "__main__":
    main()
