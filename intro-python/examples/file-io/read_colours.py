# Opening this way is not the best practice. It is safer to
# use the "with" keyword. See below.
colours = open("colours.txt")
cout = open("colours-out.txt", "w")

for c in colours: # c will include a newline character!
    if c.lower().startswith("i"):
        break
    cout.write(c)

colours.close()
cout.close()


# This is the safer method
with open("colours.txt") as colours:
    with open("colours-out-safe.txt", "w") as cout:
        for line in colours.readlines():
            if line.lower().startswith("i"):
                break
            cout.write(line)
# Don't need to close it using the "with" keyword.