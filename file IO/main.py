name = input("what is your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
