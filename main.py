import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sort_dictionary_by_value
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    directory = sys.argv[1]
    with open(directory) as file:
        content = file.read()
    num_characters = get_num_characters(content)

    num_words = get_num_words(content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book at {directory}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count -------")
    sort_dictionary_by_value(num_characters)
    print("============= END ===============")
if __name__ == "__main__":
    main()