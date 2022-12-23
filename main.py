RPS = {
    "Rock": 2,
    "Paper": 1,
    "Scissors": 0,
}
players={
"Player1" : "",
"Player2" : ""
}


def whoWinTheGame(players):
    if abs(RPS[players[list(players.keys())[0]]]-RPS[players[list(players.keys())[1]]])==1:
        winner = list(players.keys())[list(players.values()).index(list(RPS.keys())[list(RPS.values()).index(min(RPS[players[list(players.keys())[0]]], RPS[players[list(players.keys())[1]]]))])]
        return f"Winner is {winner}"
    elif abs(RPS[players[list(players.keys())[0]]]-RPS[players[list(players.keys())[1]]])==2:
        winner = list(players.keys())[list(players.values()).index(list(RPS.keys())[list(RPS.values()).index(max(RPS[players[list(players.keys())[0]]], RPS[players[list(players.keys())[1]]]))])]
        return f"Winner is {winner}"
    else:
        return "It is a Draw"


for i in list(RPS.keys()):
    for j in list(RPS.keys()):
        players = {
            "Player1": i,
            "Player2": j
        }
        print(f"{list(players.keys())[0]} is {i}, {list(players.keys())[1]} is {j} \n {whoWinTheGame(players)}")

### Choose 0,1,2
choice = input(f"What is your Choice: {RPS} \n")
import random
players["Player1"] = str(list(RPS.keys())[list(RPS.values()).index(int(choice))])
print(f"Your Choice is {list(RPS.keys())[list(RPS.values()).index(int(choice))]}")
players["Player2"] = str(list(RPS.keys())[list(RPS.values()).index(int(random.randint(0,2)))])
print(f'Your Opponent\'s Choice is {players["Player2"]}')

print(f'{list(players.keys())[0]} is {players["Player1"]}, {list(players.keys())[1]} is {players["Player2"]} \n {whoWinTheGame(players)}')






