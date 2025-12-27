def get_num_words(content):
    words = content.split()
    return len(words)

def get_num_characters(content):
    character_count = {}
    words = content.split()
    character = words.split()
    for char in character:
        if char.lower() not in character_count:
            character_count[char.lower()] = 1
        else:
            character_count[char] += 1
    return character_count