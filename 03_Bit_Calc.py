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
            print("Please choose a valid file type in the form of an integer, text or image")
            print()

def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter something that is more than "
        "(or equal to) {}".format(low)

        try:

            #ask user to enter a number
            response = int(input(question))

            #checks number is more than zero
            if response >= low:
                return response
                               

            #Outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
                 print(error)
                 print()


def text_bits():

    print()
    var_text = input("Enter some text: ")

    var_length = len(var_text)
    num_bits = 8 * var_length

    print()
    print("\'{}\' has {} characters . . .".format(var_text, var_length))
    print("# of bits is {} x 8 . . .".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_length))
    print()

    return ""

def image_bits():

    image_width = num_check("Image width? ", 1)
    image_height = num_check("Image height? ", 1)

    num_pixels = image_width * image_height

    num_bits = num_pixels * 24

    print()
    print("# of pixels = {} x {} = {}".format(image_height, image_width, num_pixels))

    print("# bits = {} x 24 = {}". format(num_bits, num_bits))
    return ""

def int_bits():

    var_integer = num_check("Please enter an integer: ", 0)

    var_binary = "{0:b}".format(var_integer)

    num_bits = len(var_binary)

    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""

statement_generator("Bit Calculator for Integers, Text & Images", "-")

keep_going = " "
while keep_going == " ":

    data_type = user_choice()
    print("You Chose", data_type)

    if data_type == "integer":
        var_integer = num_check("Enter an integer: ", 0)

    elif data_type == "image":
        image_width = num_check("Image width? ", 1)
        print()
        image_height = num_check("Image height? ", 1)

    else:
        var_text = input("Enter some text: ")


