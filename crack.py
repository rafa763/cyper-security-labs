# Get the shadow from the user
shadow = input("shadow:")

# Initialize the counter to know the line number
counter = 0

# Open the file with the hashes
with open("hash.txt", "r") as file:
    # Iterate over each line
    for line in file:
        counter += 1
        # Compare the hash with the shadow
        if line.strip() == shadow:
            break
# Counter to comapre with the first
linecount = 0
# Open the file with the passwords
with open("password.txt", "r") as file2:
    # Iterate over each line
    for line in file2:
        linecount += 1
        # If the two counter are equal then we found the password
        if (linecount == counter):
            # Print the password
            print(line)
