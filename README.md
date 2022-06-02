## zuri-module
A python implementation of the `Rock-Paper-Scissors` game.

This project uses the built in random library to help the computer select random choices. 
You can click [here](https://docs.python.org/3.8/library/random) to know more about the random module.

The operation of the game is such that whenever a winner is found (either the CPU or the user/player), the program
prints the winner and is then terminated.

For the classical `Rock-Paper-Scissors` game:
    
    Rock beats Scissors,
    Paper beats Rock,
    Scissors beats Paper

This can be seen as a circular comparison, that is

    Rock > Scissors > Paper > Rock

The scripts sees it that Rock is greater than Paper and so on. Notice that each option (Rock, Paper, Scissors) is only greater/ can only beat a singular option i.e Rock can only beat scissors but not paper, so we say Rock is greater than scissors but less than papper (Though the script only implements a greater than)

This comparison in this script is implemented with the help of a dictionary. The keys of the dictionary are the valid game options i.e 'R' (for Rock), 'P' (for paper) and 'S' (for Scissors). While the value of each dict is that singular options which the key is greater than. The dictionary looks like this : 

    options = {'R' : 'S', 'S' : 'P', 'P' : 'R'}

With the help of this dictionary, comparison is made way simpler and it also eliminates the need of multiple if statements as such:

    def comparison(x,y)
        # check if x is Rock
        if x == 'Rock':
            # Rock is only greater than Scissors
            if p == 'Scissors':
                return True
            else:
                return False
        # check if x is Paper
        if x == 'Paper':
            # Paper is only greater than Rock
            if p == Rock:
                return True
            else:
                return False
        # check if x is Scissors
        if x == 'Scissors':
            # Scissors only beats Paper
            # using: result if cond else another
            return True if p == 'Paper' else False


With the help of the dictionary, the whole code above is reduced to this

    options = {'R' : 'S', 'S' : 'P', 'P' : 'R'}

    def comparison(x,p):
    # x and y are assumed to be valid keys in options
    if p == options[x]:
        return True
    else:
        return False

This fuction can be done in a single line using the expression

    return True if p == option[x] else False

making it way simpler than the nested if statements