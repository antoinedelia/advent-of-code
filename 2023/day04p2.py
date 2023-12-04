x = open(0).read()

additional_cards = {i: 1 for i in range(len(x.splitlines()))}

total_scratchcards = 0

for i, line in enumerate(x.splitlines()):
    while additional_cards[i] > 0:
        total_scratchcards += 1
        numbers = line.split(": ")[1]
        win_numbers, my_numbers = [stack.split() for stack in numbers.split(" | ")]
        matching_numbers = set(win_numbers) & set(my_numbers)
        if matching_numbers:
            for bonus in range(len(matching_numbers)):
                bonus_card_index = i + bonus + 1
                additional_cards[bonus_card_index] += 1
        additional_cards[i] -= 1

print(total_scratchcards)
