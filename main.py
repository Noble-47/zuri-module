"""
A python implementation of the `Rock-Paper-Scissors` game.
A console app
"""
import random


class RPS:
    options = {"S": "P", "P": "R", "R": "S"}

    def __init__(self, pick, name):
        self.pick = pick
        self.name = name

    def __gt__(self, x):
        # S > p  P > R R > S
        if x.pick == self.options[self.pick]:
            return True
        else:
            return False


option_list = ["R", "P", "S"]
mapping = {
    "R": RPS(pick="R", name="Rock"),
    "P": RPS(pick="P", name="Papper"),
    "S": RPS(pick="S", name="Scissors"),
}


def play():
    print(
        'Enter your choice ("R" for Rock, "P" for Paper, "S" for Scissors) : ', end=""
    )
    user_pick = input().upper()
    # validate user's pick
    if user_pick in option_list:
        comp_pick = random.choice(option_list)
        return evaluate_winner(user_pick, comp_pick)

    else:
        print(
            f"\n {user_pick} is an Invalid option. \
         Please select either 'R', 'P' or 'S'"
        )


def evaluate_winner(user_pick, comp_pick):
    p1 = mapping.get(user_pick, None)
    p2 = mapping.get(comp_pick, None)
    # check that p1 and p2 has values
    assert p1
    assert p2

    if p1.pick == p2.pick:
        # Its a tie
        print(
            f"player({p1.name}) : CPU({p2.name}) \
                \nIt's a Tie"
        )
        return False

    if p1 > p2:
        # p1 wins
        print(
            f"player({p1.name}) : CPU({p2.name}) \
                \nPlayer Wins!!!"
        )
    else:
        # p2 wins
        print(
            f"player({p1.name}) : CPU({p2.name}) \
                \nCPU Wins!!!"
        )
    return True


def game():
    print("Welcome To My Python Implementation Of Rock Paper Scissors")
    winner = False
    while not winner:
        winner = play()


if __name__ == "__main__":
    game()
