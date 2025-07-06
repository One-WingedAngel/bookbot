
def count_words(text):
    word_count = 0

    split_content = text.split()

    for word in split_content:
        word_count +=1 
    
    return word_count

def count_characters(text):
    text = text.lower()
    char = {}

    for c in text:
        if c in char:
            char[c] +=1
        else:
            char[c] = 1
    return char

def sorted_on(dict):
    return dict["num"]   

def sort_characters(dict):
    sorted  = []

    for character in dict: 
        count = dict[character]

        char_dict = {}
        char_dict["char"] = character
        char_dict["num"] = count
        sorted.append(char_dict)

    sorted.sort(reverse=True,key=sorted_on)
    return sorted

    



