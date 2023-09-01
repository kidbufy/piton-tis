import random

category_list = [['kopek', 'kedi', 'dinazor', 'balik'], ['elma', 'armut', 'karpuz', 'balkabagi']]
word = None
index = None
hangman = ["|\n"
          "|\n"
          "|", "|---\n"
               "|\n"
               "|\n"
               "|\n", "|---\n"
                    "|  |\n"
                    "|\n"
                    "|\n", "|---\n"
                         "|  |\n"
                         "|  O\n"
                         "| -|-\n"
                         "  / \*\n"]
game_map = []
used_letters = []

def ask_for_category():
    categories = ['Hayvanlar','Meyveler']
    print(categories)
    while True:
        category = input("Which category you want to play: ").capitalize()
        if category in categories:
            index = categories.index(category)
            return choose_a_word(category_list[index])
        else:
            print("You should choose a category from the category list.")

def choose_a_word(list_of_words):
    return random.choice(list_of_words)

def create_game():
    for i in word:
        game_map.append("_")
    print(game_map)

def check_the_answer(letter):
    global count

    index_of_letter = -1
    if letter in word and letter not in used_letters:
        for i in word:
            index_of_letter += 1
            if i == letter:
                game_map[index_of_letter] = i
        used_letters.append(letter)
    elif letter in used_letters:
        print("You already used that letter.")
    else:
        count = count + 1
        print('')
        print(hangman[count])
        used_letters.append(letter)
    print('')
    print(game_map)
    print('')
def check_win():
    if "_" not in game_map:
        print("Congratulations the word was "+ word + ".")
        exit()






word = ask_for_category()

create_game()
count = -1
while count != 3:
    print("Used letters: ",end="")
    print(used_letters)
    move = input("\nChoose a letter: ")
    check_the_answer(move)
    check_win()
print("The word was "+word+". Sorry.")









