def get_num_words(content):
    words = content.split()
    return len(words)

def get_num_characters(content):
    character_count = {}
    for char in content:
        if char.lower() not in character_count:
            character_count[char.lower()] = 1
        else:
            character_count[char.lower()] += 1
    return character_count
def sort_dictionary_by_value(character_count):
    return dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))