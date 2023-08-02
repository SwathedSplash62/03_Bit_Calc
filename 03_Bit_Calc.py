# function goes here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

statement_generator("Hello World", "-")

def user_choice():

    valid = False
    while not valid:

        response = "File type (integer / text / image): ".lower()

        if response == "text" or response == "t":
            return response

        else:
            print("Please choose a vaild file type :((")
            print()

data_type = user_choice()