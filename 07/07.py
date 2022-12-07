from dataclasses import dataclass


@dataclass
class File:
    path: str
    size: int


with open("07/07_input.txt") as f:
    shell = f.read().splitlines()

files: list[File] = []
current_path = "/"
total_size = 0

for line in shell:
    if line.startswith("$ cd "):
        new_dir = line.split("$ cd ")[1]
        if new_dir == "/":
            current_path = "/"
        elif new_dir == "..":
            current_path = "/".join(current_path.split("/")[:-2]) + "/"
        else:
            current_path += f"{new_dir}/"
    elif line.startswith("dir") or line.startswith("$ ls"):
        continue
    else:
        size, file_name = line.split()
        total_size += int(size)
        new_file = File(f"{current_path}{file_name}", int(size))
        files.append(new_file)

directory_size = {}

for file in files:
    all_directories = file.path.split("/")[1:-1]
    current_dir = ""
    for dir in all_directories:
        # We do this in case we have duplicate folder name in different places
        current_dir = current_dir + "/" + dir
        if current_dir not in directory_size:
            directory_size[current_dir] = 0
        directory_size[current_dir] += file.size

max_size = 100000
sum_of_max_size = sum(size for size in directory_size.values() if size <= max_size)

print(sum_of_max_size)

# Part 2

total_disk_space_available = 70000000
unused_space_required = 30000000
current_unused_space = total_disk_space_available - total_size

directory_to_delete = min(
    [size for size in directory_size.values() if size >= unused_space_required - current_unused_space]
)
print(directory_to_delete)
