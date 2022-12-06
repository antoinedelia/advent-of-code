with open("06/06_input.txt") as f:
    stream = f.read()


def get_start_marker(distinct_characters: int) -> int:
    for i, elem in enumerate(
        ["".join(item) for item in zip(*[stream[n:] for n in range(distinct_characters)])], start=distinct_characters
    ):
        if len(set(elem)) == len(elem):
            return i


print(get_start_marker(4))
print(get_start_marker(14))
