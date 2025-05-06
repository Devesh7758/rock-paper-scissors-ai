def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    if len(opponent_history) < 2:
        return "R"

    last = opponent_history[-2]
    transition_table = {"R": {"R": 0, "P": 0, "S": 0},
                        "P": {"R": 0, "P": 0, "S": 0},
                        "S": {"R": 0, "P": 0, "S": 0}}

    for i in range(len(opponent_history) - 1):
        prev = opponent_history[i]
        next = opponent_history[i + 1]
        if prev in transition_table and next in transition_table[prev]:
            transition_table[prev][next] += 1

    prediction = max(transition_table[last], key=transition_table[last].get)

    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[prediction]
