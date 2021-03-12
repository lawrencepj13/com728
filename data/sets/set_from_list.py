#function to ask user input x7 and return observations stored in a list

def observed():
    observations = []
    for count in range(7):
        print("Please enter an observation:")
        observations.append(input())

    return observations


#run the above function and collate the data into a set to then print iterations of each - stored in data
def run():
    print("Counting Observations:")
    user_observation = observed()
    user_observation_set = set()
    for observation in user_observation:
        data = (observation, user_observation.count(observation))
        user_observation_set.add(data)
    for data in user_observation_set:
        print(f"{data[0]} observed {data[1]} times!")

run()
#if entering more than 2 different observations, the print function will still work!
