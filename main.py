def main():


    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        letter_count = char_count(file_contents)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)} words found in the document")
    print("")

    letter_count.sort(reverse=True, key=sort_on)

    for letter_dict in letter_count:
        print(f"The '{letter_dict['letter']}' character was found {letter_dict['num']} times")

    print("--- End report ---")



def word_count(text):
    return len(text.split())

def char_count(text):
    letter_count = {}
    letter_set = set(list(text.lower()))
    for letter in letter_set:
        letter_count[letter] = text.lower().count(letter)

    letter_list = []
    for letter in letter_count:
        if(letter.isalpha()):
            letter_list.append({"letter": letter, "num": letter_count[letter]})
    
    return letter_list

def sort_on(dict):
    return dict["num"]

main()