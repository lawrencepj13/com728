def patterns():
    print("Dictionary:")
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences

def display_keys(data):
    sequences = data
    print("Keys:")
    for key in sequences:
        print(key)

def display_values(data):
    sequences = data
    print("Values:")
    for value in sequences.values():
        print(value)


def display_items(data):
    sequences = data
    print("Pairs:")
    for key, value in sequences.items():
        print(f"{key}: {value}")

def run():
    print(patterns())
    display_keys(patterns())
    display_values(patterns())
    display_items(patterns())


run()