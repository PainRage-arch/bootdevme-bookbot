from stats import get_num_words
from stats import get_num_characters
def main():
    
    with open("books/frankenstein.txt") as file:
        content = file.read()
    
    num_words = get_num_words(content)
    print(f"Found {num_characters} total characters")    
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()