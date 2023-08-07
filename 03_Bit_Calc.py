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

statement_generator("Bit Calcuator for Integers, Text & Immages", "-")

def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter something that is more than "
        "(or equal to) {}".format(low)

        try:

            #ask user to enter a number
            response = (input(question))

            #checks number is more than zero
            if response > low:
                return response
                               

            #Outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
                 print(error)
                 print()

def user_choice():

    valid = False
    while not valid:

        response = input("File type (integer / text / image): ").lower()

        if response == "text" or response == "t" or response == "txt":
            return "Text"

        if response == "integer" or response == "int":
            return "An Integer"

        if response == "image" or response == "P" or response == "img":
            return "An Image"

        else:
            print("Please choose a vaild file type in the form of an integer, text or image")
            print()

data_type = user_choice()
print("You Chose", data_type)

print()

keep_going = ""
while keep_going =="":

    keep_going = input("Press <enter> for an integer or any key for an image")

print()