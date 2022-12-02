from enum import Enum


class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


with open("02/02_input.txt") as f:
    rounds = f.read().splitlines()

MAP_POINTS = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

MAP_LETTER_RESULT = {
    "X": Result.LOSS,
    "Y": Result.DRAW,
    "Z": Result.WIN,
}

RESULT_MAP = {
    "A": {
        "X": Result.DRAW,
        "Y": Result.WIN,
        "Z": Result.LOSS,
    },
    "B": {
        "X": Result.LOSS,
        "Y": Result.DRAW,
        "Z": Result.WIN,
    },
    "C": {
        "X": Result.WIN,
        "Y": Result.LOSS,
        "Z": Result.DRAW,
    },
}

total_score_part_one = 0
total_score_part_two = 0

for round in rounds:
    opponent_move, your_move = round.split(" ")
    total_score_part_one += MAP_POINTS[your_move]
    total_score_part_one += RESULT_MAP[opponent_move][your_move].value

    expected_outcome = MAP_LETTER_RESULT[your_move]
    your_real_move = [k for k, v in RESULT_MAP[opponent_move].items() if v == expected_outcome][0]
    total_score_part_two += MAP_POINTS[your_real_move]
    total_score_part_two += RESULT_MAP[opponent_move][your_real_move].value


print(total_score_part_one)
print(total_score_part_two)
