from stats import get_num_words
from stats import get_num_characters
from stats import sort_dictionary_by_value
def main():
    
    with open("books/frankenstein.txt") as file:
        content = file.read()
    num_characters = get_num_characters(content)
    num_characters = sort_dictionary_by_value(num_characters)
    num_words = get_num_words(content)
      
    print(f"Found {num_words} total words")
    print(f"Found {num_characters} characters") 
if __name__ == "__main__":
    main()