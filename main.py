def main():
        path_to_file = "books/Frankenstein.txt"
        with open(path_to_file) as f:
             text = f.read()
             word_count = Word_Count(text)
             characters = Character_Count(text) 
             sorted_characters = sort_on(characters)
             report(word_count, sorted_characters)
        
def Word_Count(book):
       word_total = len(book.split())
       return word_total

def Character_Count(book):
       lowercase_book = book.lower()
       totals = {}
       for i in range(len(lowercase_book)):
             if lowercase_book[i] in totals:
                    totals[lowercase_book[i]] += 1
             elif lowercase_book[i].isalpha():
                    totals[lowercase_book[i]] = 1
       return totals

def sort_on(diction):
       sorted_list = dict(sorted(diction.items(), key=lambda item: item[1], reverse=True))
       return sorted_list

def report(word_count, character_count):
       print("--- Begin report of books/frankenstein.txt ---")
       print(f"{word_count} words found in the document")    
       for c in character_count:
            print(f"The {c} character was found {character_count[c]} times")     
       print("--- End report ---")

main()