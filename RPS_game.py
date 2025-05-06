import random

def play(player1, player2, num_games=1000, verbose=False):
    results = {"player1": 0, "player2": 0, "tie": 0}
    p1_history, p2_history = "", ""
    for _ in range(num_games):
        p1_move = player1(p2_history)
        p2_move = player2(p1_history)
        p1_history = p1_move
        p2_history = p2_move
        if p1_move == p2_move:
            results["tie"] += 1
        elif (p1_move == "R" and p2_move == "S") or (p1_move == "P" and p2_move == "R") or (p1_move == "S" and p2_move == "P"):
            results["player1"] += 1
        else:
            results["player2"] += 1
    print(results)

def quincy(prev_play):
    return "R"

def abbey(prev_play):
    return "P"

def kris(prev_play):
    return "S"

def mrugesh(prev_play):
    return random.choice(["R", "P", "S"])
