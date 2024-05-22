import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def caesar(text, shift, direction):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            if direction == "decode":
                index = alphabet.index(letter) - shift
                if index < 0:
                    index += 51
                cipher_text += alphabet[index]
            elif direction == "encode":
                index = alphabet.index(letter) + shift
                if index > 51:
                    index -= 51
                cipher_text += alphabet[index]
            else:
                print("Invalid input:" + direction)
        else:
            cipher_text += letter
    return cipher_text
print(art.logo)
active = True
while active:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if (direction == "encode") or (direction == "decode"):
        text = input("Type your message:\n")
        try:
            shift = (int(input("Type the shift number:\n")) % 52)
            print(caesar(text, shift, direction))

            choice = input("Press enter to return or X to exit\n")
            if choice != "":
                active = False
        except ValueError:
            print("The input was not a valid number.")
    else:
        print("\nNot a valid input.")
