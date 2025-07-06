from stats import count_words,count_characters,sort_characters
import sys

def main():
    if len(sys.argv) ==2 :
        text = get_book_text(sys.argv[1])
        
        word_count = count_words(text)
        character_count = count_characters(text)
        sort = sort_characters(character_count)
        print_report(sys.argv[1],word_count,sort)
    
    else:
        sys.stdout.write("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
            

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_report(book_path, num_words,sort):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for c in sort:
        if c["char"].isalpha():
            num = c["num"]
            print(f"{c["char"]}: {num}") 


main()
