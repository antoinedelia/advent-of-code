import re
from dataclasses import dataclass

IS_TEST = True


@dataclass
class Valve:
    name: str
    flow_rate: int
    connected_valves: list[str]


with open("16/16_test_input.txt" if IS_TEST else "16/16_input.txt") as f:
    infos = f.read().splitlines()

valves: list[Valve] = []
for info in infos:
    valve1, *connected_valves = re.findall("[A-Z]{2}", info)
    flow_rate = list(map(int, re.findall("\d+", info)))[0]
    valve = Valve(valve1, flow_rate, connected_valves)
    print(valve)
    valves.append(valve)

combinations_done = set()
while True:

    for i in range(1, 31):
        print(f"=== Minute {i} ===")
