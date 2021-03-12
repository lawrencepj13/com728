#function to ask user input x5 and return observations stored in a list

def observed():
    observations = []
    for count in range(5):
        print("Please enter an observation:")
        observations.append(input())

    return observations
#function to remove a specified observation using simple if statement
def remove_observations(observation_list):
    print("Do you wish to remove an observation? (yes/no")
    response = input()
    if response == "yes":
        print("What observation do you wish to remove?")
        discarded_response = input()
        observation_list.remove(discarded_response)
        print("Done!")
    else:
        print("Nothing will be changed")

#run function that prints appended observations
def run():
    user_observation = observed()
    remove_observations(user_observation)
    user_observation_set = set()
    for observation in user_observation:
        data = (observation, user_observation.count(observation))
        user_observation_set.add(data)
    for data in user_observation_set:
        print(f"{data[0]} observed {data[1]} times!")


run()