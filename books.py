def count_unique_words(file_path):
    """
    Reads a book from a local text file and counts words that appear only once.

    :param file_path: Path to the book file (e.g., "book1.txt")
    :return: Number of words that appear only once
    """
    punctuation = ",.?!';\":-=(){}"

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    word_count = {}  # Dictionary to store word frequencies
    lines = text.splitlines()  # Split text into lines

    for line in lines:
        for p in punctuation:
            line = line.replace(p, " ")  # Remove punctuation
        words = line.split()
        for word in words:
            word = word.lower()  # Convert to lowercase
            word_count[word] = word_count.get(word, 0) + 1  # Count occurrences

    # Count words that appear only once
    unique_count = sum(1 for count in word_count.values() if count == 1)

    return unique_count

# Provide the local paths to the books
book1_path = "romeo_and_juliet.txt"  # Replace with your actual file path
book2_path = "pride_and_prejudice.txt"  # Replace with your actual file path

# Count unique words for each author
book1_unique_count = count_unique_words(book1_path)
book2_unique_count = count_unique_words(book2_path)

# Print results
print(f"Book 1 has {book1_unique_count} unique words.")
print(f"Book 2 has {book2_unique_count} unique words.")

# Determine the author with more unique words
if book1_unique_count > book2_unique_count:
    print("Book 1's author used more unique words.")
else:
    print("Book 2's author used more unique words.")
