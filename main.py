def main():
    
    with open("books/frankenstein.txt") as file:
        content = file.read()
        
        print(content)
        return content
if __name__ == "__main__":
    main()