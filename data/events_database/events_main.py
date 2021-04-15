import events_process


def menu():
    print("Please enter one of the following options:")
    print("""[1] Display presenters
[2] Display events
[3] Display presenters for event
[4] Display events for presenter""")
    print()
    print("Your selection:")
    response = int(input())
    return response


def run():
    selection = menu()
    if selection == 1:
            print(f"Your selection is {selection}")
            events_process.display_presenters_with_orgs()
    else:
        print("Please enter a valid response")




if __name__ == "__main__":
    run()