def read_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_counts(text):
    count = text.split()
    return len(count)

def main():
    path_to_file = "books/frankenstein.txt"  # Path to your file
    content = read_file(path_to_file)
    print(content)

    words = word_counts(content)
    print(f"The Frankenstein book contains {words} words.")


main()