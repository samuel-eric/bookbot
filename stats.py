def get_num_word(text):
    return len(text.split())

def count_char(text):
    count = {}
    for word in text:
        for char in word:
            lowercase = char.lower()
            if lowercase in count:
                count[lowercase] += 1
            else:
                count[lowercase] = 1
    return count

def sort_count_char(count):
    list_count_char = []
    for char in count:
        list_count_char.append({
            "character": char,
            "count": count[char]
        })
    list_count_char.sort(reverse=True, key=sort_on)
    return list_count_char

def sort_on(dict):
    return dict["count"]