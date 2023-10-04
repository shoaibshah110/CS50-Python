#print("#")
#print("#")
#print("#")


#for i in range(3):
#    print("#")


def main():
    print_column(3)
    print_row(3)

def print_column(height):
    for i in range(height):
        print("#")

def print_row(width):
        print("?" * width)




main()