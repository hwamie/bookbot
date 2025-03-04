import sys
from stats import get_text_numwords, get_text_numchars, sort_chardict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


try: 
    book_contents = get_book_text(sys.argv[1])
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

wordcount = get_text_numwords(book_contents)
charcount = get_text_numchars(book_contents)
sorted_list = sort_chardict(charcount)

print(f"Found {wordcount} total words")

for item in sorted_list:
    if item['char'].isalpha():
        print(f"{item['char']}: {item['count']}")

