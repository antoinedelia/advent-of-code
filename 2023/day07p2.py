x = open(0).read().splitlines()

plays = []

for line in x:
    plays.append((line.split()[0], int(line.split()[1])))

order = "AKQT987654321J"


def sort_string(input: str):
    input: list = list(input)
    input.sort()
    input = "".join(input)
    return input


def is_five_of_a_kind(hand: str):
    hand = hand.replace("J", "")
    if not hand:
        return True
    return hand == len(hand) * hand[-1]


def is_four_of_a_kind(hand: str):
    original_hand = hand
    for char in order:
        hand = original_hand
        hand = hand.replace("J", char)
        hand = sort_string(hand)
        if (4 * hand[0]) in hand or (4 * hand[1]) in hand or (4 * hand[-1]) in hand:
            return True
    return False


def is_full_house(hand: str):
    original_hand = hand
    for char in order:
        hand = original_hand
        hand = hand.replace("J", char)
        hand = sort_string(hand)
        if ((3 * hand[0]) in hand and hand[3] == hand[4]) or ((3 * hand[-1]) in hand and hand[0] == hand[1]):
            return True
    return False


def is_three_of_a_kind(hand: str):
    original_hand = hand
    for char in order:
        hand = original_hand
        hand = hand.replace("J", char)
        hand = sort_string(hand)
        if (3 * hand[0]) in hand or (3 * hand[1]) in hand or (3 * hand[-1]) in hand:
            return True
    return False


def is_two_pair(hand: str):
    original_hand = hand
    for char in order:
        hand = original_hand
        hand = hand.replace("J", char)
        hand = sort_string(hand)
        if (
            (hand[0] == hand[1] and hand[2] == hand[3])
            or (hand[1] == hand[2] and hand[3] == hand[4])
            or (hand[2] == hand[3] and hand[3] == hand[4])
            or (hand[0] == hand[1] and hand[3] == hand[4])
        ):
            return True
    return False


def is_one_pair(hand: str):
    original_hand = hand
    for char in order:
        hand = original_hand
        hand = hand.replace("J", char)
        hand = sort_string(hand)
        if (hand[0] == hand[1]) or (hand[1] == hand[2]) or (hand[2] == hand[3]) or (hand[3] == hand[4]):
            return True
    return False


def is_high_card(hand: str):
    original_hand = hand
    for char in order:
        hand = original_hand
        hand = hand.replace("J", char)
        if len(set(hand)) == len(hand):
            return True
    return False


possible_types = {
    "FiveOfAKind": {"func": is_five_of_a_kind, "plays": []},
    "FourOfAKind": {"func": is_four_of_a_kind, "plays": []},
    "FullHouse": {"func": is_full_house, "plays": []},
    "ThreeOfAKind": {"func": is_three_of_a_kind, "plays": []},
    "TwoPair": {"func": is_two_pair, "plays": []},
    "OnePair": {"func": is_one_pair, "plays": []},
    "HighCard": {"func": is_high_card, "plays": []},
}

for play, bid in plays:
    for type, values in possible_types.items():
        if values["func"](play):
            values["plays"].append((play, bid))
            break

tot = 0

rank = 1
for type, values in dict(reversed(possible_types.items())).items():
    if not values["plays"]:
        continue
    sorted_plays = sorted([(play, bid) for play, bid in values["plays"]], key=lambda word: [order.index(c) for c in word[0]])
    for play, bid in reversed(sorted_plays):
        tot += bid * rank
        rank += 1

print(tot)
