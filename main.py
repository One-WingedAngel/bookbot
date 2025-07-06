from stats import count_words,count_characters,sort_characters
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) ==2 :
        text = get_book_text(sys.argv[1])
        
        word_count = count_words(text)
        print(f"Found {word_count} total words")
        character_count = count_characters(text)
        print(character_count)
        sort = sort_characters(character_count)


        for c in sort:
            if c["char"].isalpha():
                num = c["num"]
                print(f"{c["char"]}: {num}") 
    else:
        sys.stdout.write("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
            

main()
