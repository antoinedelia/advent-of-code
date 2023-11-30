import copy

IS_TEST = False
IS_PART_ONE = True

with open("17/17_test_input.txt" if IS_TEST else "17/17_input.txt") as f:
    jet_pattern = f.read()

ROCKS: list[list[complex]] = [
    [1 + 1j, 2 + 1j, 3 + 1j, 4 + 1j],
    [1 + 2j, 2 + 1j, 2 + 2j, 2 + 3j, 3 + 2j],
    [1 + 1j, 2 + 1j, 3 + 1j, 3 + 2j, 3 + 3j],
    [1 + 1j, 1 + 2j, 1 + 3j, 1 + 4j],
    [1 + 1j, 2 + 1j, 1 + 2j, 2 + 2j],
]
WIDTH = 7.0
ROCKS_TO_FALL = 2022 if IS_PART_ONE else 1_000_000_000_000
EXPECTED_TEST_RESULT = 3068 if IS_PART_ONE else 1_514_285_714_288

remaining_patterns = jet_pattern
patterns_used = 0
can_fall = True

highest_point: complex = 0j
blocked: set[complex] = set()
blocked.update([1, 2, 3, 4, 5, 6, 7])

rocks_fallen = 0


while True:
    for rock in copy.deepcopy(ROCKS):
        if rocks_fallen == ROCKS_TO_FALL:
            print(int(highest_point.imag))
            if IS_TEST:
                print(f"Expected result: {EXPECTED_TEST_RESULT}")
            exit(0)
        can_fall = True
        # Init rock to be 3 units above highest rock, and 2 right from wall
        for i in range(len(rock)):
            rock[i] += highest_point + 3j + 2
        while can_fall:
            for pattern in remaining_patterns:
                # Try to move the rock
                can_move = True
                change = -1 if pattern == "<" else 1
                for tile in rock:
                    if tile.real + change <= 0 or tile.real + change > WIDTH or tile + change in blocked:
                        can_move = False
                        break
                if can_move:
                    for i in range(len(rock)):
                        rock[i] += change
                patterns_used += 1

                # Try to make the rock fall
                for tile in rock:
                    if tile - 1j in blocked:
                        can_fall = False
                        rocks_fallen += 1
                        blocked.update([tile for tile in rock])
                        highest_point = max(highest_point.imag, *[tile.imag for tile in rock]) * 1j
                        break
                if not can_fall:
                    break
                if can_fall:
                    for i in range(len(rock)):
                        rock[i] -= 1j

            if can_fall:
                remaining_patterns = jet_pattern
                patterns_used = 0

        # Update remaining patterns
        remaining_patterns = remaining_patterns[patterns_used:]
        patterns_used = 0
