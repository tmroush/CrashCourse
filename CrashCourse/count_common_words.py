
def count_word(filename, word):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"sorry, the file {filename} does not exist.")
    else:
        num_words = contents.lower().count(word)
        print(f"There are approximately {num_words} '{word}' in {filename}")


filename = 'alice.txt'
count_word(filename, 'the')
count_word(filename, 'the ')
count_word(filename, 'these')
