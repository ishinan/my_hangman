'''
hangman.py
'''

def print_status(word, chances):
    '''
    print status
    '''
    number_of_characters = len(word)
    list_of_characters = [ x for x in word ]
    list_of_temp_words = [ " " for i in range(number_of_characters) ] 
    underscores = "_ " * number_of_characters
    number_of_found_chars = 0

    print("!!! Let's start !!!")
    while chances > 1:
        chances -= 1
        list_found_chars = [] 

        found_chars = ' '.join(list_of_characters)

        list_found_chars = ' '.join(list_of_temp_words)

        print(f"""
        {found_chars}
        {list_found_chars}
        {underscores}
        ***************************
        Total characters: {number_of_characters}
        Chanecs to guess: {chances}
        ***************************
        """)
        if number_of_found_chars == number_of_characters:
            print("Good Job!")
            break

        answer = input("Pick a character:?[q to quit] ")

        if answer in ['q', 'quit']:
            break
        for i, c in enumerate(list_of_characters):
            if answer == list_of_characters[i]:
                list_of_temp_words[i] = list_of_characters[i]
                number_of_found_chars += 1


def hangman():
    '''
    All hangman
    '''
    word = "hello"
    offset = 3
    number_of_chances = offset + len(word)
    print_status(word, number_of_chances)



def main():
    hangman()

if __name__ == "__main__":
    main()