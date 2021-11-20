#get the shadow from the user
shadow = input("shadow:")

counter = 0
with open("hash.txt", "r") as file:
    #reader = file.read()
    for line in file:
        counter += 1
        if line.strip() == shadow:
            break

linecount = 0
with open("password.txt", "r") as file2:
    for line in file2:
        linecount += 1
        if (linecount == counter):
            print(line)