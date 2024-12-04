def count_characters(text):
    """Counts the occurrences of each character in a string (case-insensitive)."""
    text = text.lower()
    char_counts = {}

    for char in text:
        if char.isalnum():
            char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts

def count_words(text):
    """Counts the number of words in a string."""
    words = text.split()
    return len(words)

def main():
    """Reads 'frankenstein.txt' and prints a report with word and character counts."""
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_counts = count_characters(file_contents)

    # --- Generate the report ---
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    # Sort character counts in descending order
    sorted_char_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()