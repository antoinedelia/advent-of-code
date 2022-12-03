from string import ascii_letters

with open("03/03_input.txt") as f:
    items = f.read().splitlines()

MAP_LETTER_PRIORITY = {}
for i, letter in enumerate(ascii_letters, start=1):
    MAP_LETTER_PRIORITY[letter] = i

total_priority_part_one = 0
total_priority_part_two = 0

last_three_items = []

for i, item in enumerate(items, start=1):
    # First part
    first_compartment, second_compartment = item[: len(item) // 2], item[len(item) // 2 :]
    common_character = "".join(set(first_compartment).intersection(second_compartment))
    total_priority_part_one += MAP_LETTER_PRIORITY[common_character]

    # Second part
    last_three_items.append(item)
    if i % 3 == 0:
        common_character_one = "".join(set(last_three_items[0]).intersection(last_three_items[1]))
        common_character_two = "".join(set(common_character_one).intersection(last_three_items[2]))
        total_priority_part_two += MAP_LETTER_PRIORITY[common_character_two]
        last_three_items = []

print(total_priority_part_one)
print(total_priority_part_two)
