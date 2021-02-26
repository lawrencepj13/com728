def search(path):
    with open(f"{path}") as file:
        print("Searching...")
        for line in file:
            print(f"Looked in {line.strip()}")
        print("...Done!")
def run():
    search("library.txt")
run()
