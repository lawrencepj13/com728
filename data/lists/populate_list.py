def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    path = directions()
    for index in range(len(path)):
        print("{}: {}".format(index, path[index]))
    index = int(input())
    return path[index]


def run():
    route = []
    print("Working out escape route...")
    for count in range(5):
        route.append(menu())
    print(f"Escape route - {route}")


if __name__ == "__main__":
    run()