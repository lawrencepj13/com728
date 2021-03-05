def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return likelihoods


def run():
    value = likelihood()
    print(f"Minimum likelihood of falling: {min(value)}%")


if __name__ == "__main__":
    run()