# function that encodes the password by adding 3 to each value
def encode(password):
    p = str(password)
    s = ""
    for num in p:
        new = int(num) + 3
        if new >= 10:
            new = new - 10
        s += str(new)
    return s

# function that decodes the password by subtracting 3 from each value
def decoder(password):
    


if __name__ == '__main__':
    yes = True
    while yes == True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n\n")
        option = input("Please enter an option: ")
        if option == "1":
            pas = str(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n\n")
        elif option == "2":
            print(f"The encoded password is {encode(pas)} and the original password is {decoder(pas)}.\n\n")
        if option == "3":
            yes = False
# main function carries out the encoder() and decoder() functions with menu
