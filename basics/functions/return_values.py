#create 3 functions 1 calculates total weight and other average weight and other prompts user input
def sum_weights(beep_weight, bop_weight):
    total_weights = beep_weight + bop_weight
    return total_weights
def calc_avg_weight(beep_weight, bop_weight):
    average_weights = (beep_weight + bop_weight) /2
    return average_weights
def run():
    print("What is the weight of Beep?")
    beep_weight = float(input())
    print("What is the of Bop?")
    bop_weight = float(input())
    print("What would you like to calculate?(sum or average)")
    action = input()
    if action == "sum":
        answer = sum_weights(beep_weight, bop_weight)
        print(f"The sum of Beep and Bop's weight is {answer:.2f}")
    elif action == "average":
        answer = calc_avg_weight(beep_weight, bop_weight)
        print(f"The average of Beep and Bop's weight is {answer:.2f}")
    else:
        print("ERROR please enter correct calculation!")
run()

