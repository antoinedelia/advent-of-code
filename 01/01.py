with open("01/01_input.txt") as f:
    calories = f.read().splitlines()

list_of_calories = []
current_elf_calories = 0

for calorie in calories:
    if not calorie:
        list_of_calories.append(current_elf_calories)
        current_elf_calories = 0
    else:
        current_elf_calories += int(calorie)

list_of_calories.sort(reverse=True)
print(list_of_calories[0])
print(sum(list_of_calories[0:3]))
