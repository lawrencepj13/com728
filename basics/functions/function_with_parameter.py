#define function with parameter to plan the escape
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper":
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")

