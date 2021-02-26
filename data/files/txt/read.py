def display_chars(path, num_of_chars):
    with open(f"{path}") as file:
        data = file.read(num_of_chars == 5)
        print(data)
def display_line(path):
    with open(f"{path}") as file:
        line = file.readline().strip()
        print(line)
def display_text(path):
    with open(f"{path}") as file:
        lines = file.read()
        print(lines)
def run():
    print("The first 5 characters are:")
    display_chars("library.txt", 5)
    print()
    print("The first line is:")
    display_line("library.txt")
    print()
    print("The full text is:")
    display_text("library.txt")


if __name__ == "__main__":
    run()







