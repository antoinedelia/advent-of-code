IS_TEST = False

var_done = set()

with open("21/21_test_input.txt" if IS_TEST else "21/21_input.txt") as f:
    infos = f.read().splitlines()


symbols = ["+", "-", "*", "/"]

for info in infos:
    if any(s in info for s in symbols):
        continue
    name = info[:4]
    info = info.replace(": ", " = ")
    exec(info)
    var_done.add(name)

while len(var_done) != len(infos):
    for info in infos:
        if not any(s in info for s in symbols):
            continue
        name = info[:4]
        var1 = info[6:10]
        var2 = info[13:17]
        if var1 in locals() and var2 in locals():
            info = info.replace(": ", " = ")
            exec(info)
            var_done.add(name)

print(int(locals()["root"]))
