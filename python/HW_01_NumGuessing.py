#Seth Muhlestein
#Fin6320
##Number Guessing

menu = {'1': "Low", '2': "High", '3':"Correct"}

def greeting():
    print("Welcome to the number guessing game! \n\n")
    print("Here is how it works. You get to pick a number between 1 and 100, and I get to guess it.\n")
    print("I guarantee I can guess your number in 7 tries or less. Let's play!\n\n")

def bisector(lowBound, upBound):
    return (lowBound + upBound) // 2

def get_response():
    choice = input("Tell me, is my guess 1) low, 2) high, or 3) correct? ")
    return choice

def main():

    greeting()
    lowBound = 0
    upBound = 101
    guesses = 0
    game_over = False

    while(not game_over):
        guess = bisector(lowBound, upBound)
        print("My guess is:{}".format(guess))
        user_response = get_response()
        if menu[user_response] == "Low":
            lowBound = guess
        elif menu[user_response] == "High":
            upBound = guess
        else:
            game_over = True
        guesses += 1
    print("I correctly guessed your number {} in {} tries".format(guess, guesses))

if __name__ == "__main__":
    main()
