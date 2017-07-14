## Setup Stuff

levels = {'medium': "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions.\n", 'easy': "This section is aimed at knowning state capitals.  The capital of Colorado is ___1___.  The capital of Wyoming is ___2___.  The capital of Iowa is ___3___.  The capital of Nebraska is ___4___.  The capital of California is ___5___.\n", 'hard': "This section is aimed at random facts.  ___1___ invented the jumping jack.  The name of a male chicken is called a ___2___, while a female chicken is called a ___3___.  ___4___ was the last member of the Second Continental Congress to sign the Declaration of Independence.  The area of calm near the equator is called the ___5___\n"}

answers = {'medium':{'___1___': 'function', '___2___': 'arguments', '___3___': "nothing", '___4___': 'lists'}, 'easy':{'___1___': 'denver' , '___2___': 'cheyenne', '___3___': 'des moines', '___4___': 'lincoln', '___5___': 'sacramento' } , 'hard': {'___1___': 'john pershing' , '___2___': 'rooster', '___3___': 'hen', '___4___': 'thomas mckean', '___5___': 'doldrums'}}

###_____________


def get_vals(selected_level):
    '''
    This function will take in the level from the user (easy, medium, or hard) and then use the correct number of values that will need to be filled.
    INPUT: level as a string ('easy', 'medium', 'hard')
    OUTPUT: vals as a list with either 5 inputs or four depending on level
    '''
    if selected_level == 'hard' or selected_level == 'easy':
        vals = ['___1___','___2___','___3___','___4___','___5___']
    else:
        vals = ['___1___','___2___','___3___','___4___']
    return vals


def replace_text(text_input, val, answer):
    '''
    Take text_input and replace val with answer
    INPUT: text_input: string of text you want to look through
           val: string of the value you want to replace within text_input
           answer: string answer you want to put in val within text_input
    OUTPUT: text_input with val replaced by answer
    '''
    replaced = []
    text_lst = text_input.split()
    for word in text_lst:
        word = word.replace(val, answer)
        replaced.append(word)
    replaced = " ".join(replaced)
    return replaced


def answer_stuff(selected_level):
    '''
    The meat of our game - takes the level of the game and runs the game either forever or until the user gets all the answers correct.
    INPUT: Takes the input as either easy, medium or hard as string
    OUTPUT: None
    '''
    openings = get_vals(selected_level)
    new_text = levels[selected_level]
    for idx, val in enumerate(openings):
        answer = input("What do you think should be in the " + val + " blank?\n\n")
        while answer.lower() != answers[selected_level][val]:
            print("Oops! That wasn't quite what we were looking for... try again.\n")
            answer = input("What do you think should be in the " + val + " blank?\n\n")

        print("Nice! You got it!\n")
        new_text = replace_text(new_text, val, answer)

        print("The remaining values are shown in the text below.\n\n" + new_text)

    print("\n Congrats!  You got them all!!!  You are the king (or queen) of the world!")



def intro():
    '''
    This function will prompt the user to ask appropriate question(s)
    '''

    selected_level = input('Please enter the level you would like to play - enter exactly as shown in quotes - ("easy", "medium", "hard"):  ')

    directions = '\n \n \n You will have unlimited attempts, and the goal of the game is to fill in all of values in the blanks of the following string:\n \n'
    print(directions + levels[selected_level])
    return selected_level



def main():
    '''
    This function will control the running of the entire program
    '''
    selected_level = intro()
    answer_stuff(selected_level)


if __name__ == '__main__':
    main()
