
file_name = "example.txt"


with open(file_name, "a") as f:
    f.write("is this the new line.\n")


with open(file_name, "r") as f:
    lines = f.readlines()

last_three = lines[-5:]
for line in last_three:
    print(line.strip())
