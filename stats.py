def get_num_words(content):
    words = content.split()
    return len(words)

def get_num_characters(content):
    character_count = {}
    for char in content:
        if char.lower() not in character_count:
            character_count[char.lower()] = 1
        else:
            character_count[char] += 1
    print(character_count)
    return character_count
