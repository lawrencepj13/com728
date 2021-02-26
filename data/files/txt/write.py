def search(path):
    print("Searching...")
    sections = ""
    books = "Books:\n"
    with open(f"{path}") as file:
        for line in file:
            if line.startswith("Sections"):
                sections += line
        else:
            books += line
    print("Done!")
    return f"{sections} \n\n{books}"


def save(path, data):
    print("Saving...")
    with open(path, "w") as file:
        file.write(data)
    print("Done!")


def run():
    data = search("books.txt")
    save("books.txt", data)


run()



