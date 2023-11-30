with open("04/04_input.txt") as f:
    sections = f.read().splitlines()

number_of_fully_contained = 0
number_of_partially_contained = 0

for section in sections:
    first_elf, second_elf = section.split(",")
    first_elf_range = list(range(int(first_elf.split("-")[0]), int(first_elf.split("-")[1]) + 1))
    second_elf_range = list(range(int(second_elf.split("-")[0]), int(second_elf.split("-")[1]) + 1))

    if all(camp in second_elf_range for camp in first_elf_range) or all(
        camp in first_elf_range for camp in second_elf_range
    ):
        number_of_fully_contained += 1
    if any(camp in second_elf_range for camp in first_elf_range):
        number_of_partially_contained += 1

print(number_of_fully_contained)
print(number_of_partially_contained)
