def number_of_words(text):
    words = text.split()
    return len(words)


def character_count(text):
    dictionary = {}
    for char in text:
        char = char.lower()
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary


def sorted_dictionary(dictionary):
    sorted_list = [
        {"character": char, "count": count}
        for char, count in dictionary.items()
        if char.isalpha()
    ]
    sorted_list.sort(reverse=True, key=lambda item: item["count"])
    return sorted_list
