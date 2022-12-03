with open("inputs/input_day2_0.txt",'r' ) as f:
    lines = f.readlines()

new_lines = [x.replace('\n', '') for x in lines]

print(new_lines)

opponent_translate_table = {'a': 'r', 'b': 'p', 'c': 's'}
own_translate_table = {'x': 'r', 'y': 'p', 'z': 's'}
points_for_shape = {'x': 1, 'y': 2, 'z': 3}


def points_for_winning(hand_1, hand_2):
    winner_hand_1 = 0
    winner_hand_2 = 6
    if hand_1 == hand_2:
        return 3
    if hand_1 == 'r':
        if hand_2 == 'p':
            return winner_hand_2
        elif hand_2 == 's':
            return winner_hand_1
    elif hand_1 == 'p':
        if hand_2 == 's':
            return winner_hand_2
        elif hand_2 == 'r':
            return winner_hand_1
    elif hand_1 == 's':
        if hand_2 == 'r':
            return winner_hand_2
        if hand_2 == 'p':
            return winner_hand_1


def rpc_outcome(hand_1, hand_2):
    hand_1 = hand_1.lower()
    hand_2 = hand_2.lower()
    points = points_for_shape[hand_2]
    hand_1_translated, hand_2_translated = opponent_translate_table[hand_1], own_translate_table[hand_2]
    points += points_for_winning(hand_1_translated, hand_2_translated)
    return points


points_scored = 0
for battle in new_lines:
    points_scored += rpc_outcome(battle[0], battle[2])
print(points_scored)

lose_table = {'a': 'z', 'b': 'x', 'c': 'y'}
win_table = {'a': 'y', 'b': 'z', 'c': 'x'}
translate_opponent_to_own = {'a': 'x', 'b': 'y', 'c': 'z'}


def outcome_to_hand(hand_1, outcome):
    hand_1 = hand_1.lower()
    if outcome == 'Y':
        return translate_opponent_to_own[hand_1]
    if outcome == 'X':
        return lose_table[hand_1]
    if outcome == 'Z':
        return win_table[hand_1]


punten_ronde2 = 0
for battle in new_lines:
    punten_ronde2 += rpc_outcome(hand_1=battle[0], hand_2=outcome_to_hand(battle[0], battle[2]))
print(punten_ronde2)
