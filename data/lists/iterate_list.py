def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction")
    path = directions()
    for index in range(len(path)):
        print(f"{index}: {path[index]}")


def run():
    print(menu())


if __name__ == "__main__":
    run()