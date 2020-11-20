filename = "pi_digits.txt"
with open (filename) as file_obj:
    for line in file_obj:
        print(line)

print("no new line \n")
with open (filename) as file_obj:
    for line in file_obj:
        print(line.rstrip())