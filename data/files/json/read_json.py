import json

def read(path):
    with open("robocity.json") as file:
        data = json.load(file)
        city = data["city"]
        print(f"City name:{city}")
        population = data["population"]
        print(f"Population size:{population}")

        for bot in data ["bots"]:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats:{stats}")


def run():
    read("robocity.json")

if __name__ == "__main__":
  run()
