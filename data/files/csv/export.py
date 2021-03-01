import csv

def export(path, exported_bots):
    print("Exporting....")
    with open("exported_bots.csv", "a") as file:
        for count in range(exported_bots):
          print("Enter Bot ID:")
          bot_id = int(input())
          print("Enter Bot Name:")
          bot_name = input()
          print("Enter Bot Paint:")
          bot_paint = input()
          data = (f"{bot_id}, {bot_name}, {bot_paint}")
          file.write(data)
    print("Done!")


def run():
    export("exported_bots.csv", 2)


if __name__ == "__main__":
    run()


