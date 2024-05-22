# functions with outputs
def format_name(first_name, last_name):
    """"Takes a first and last name and returns a formatted name"""
    if first_name == "":
        return "You did not provide a first name"
    if last_name == "":
        return "You did not provide a last name"
    fname = first_name.title()
    lname = last_name.title()
    return fname + " " + lname

print("Hello " + format_name(input("What is your first name?: "), input("What is your last name?: ")))