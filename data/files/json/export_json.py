import json

def read(path):
    print("Reading:")
    with open("robocity.json") as file:
        data = json.load(file)
    print("Done!")
    return data


def save(path, data_to_save):
    print("Exporting:")
    with open("exported.json", "w") as file:
        json.dump(data_to_save, file, indent=4)
    print("Done!")


def run():
    json_data = read("robocity.json")
    save("exported.json", json_data)


if __name__ == "__main__":
    run()

