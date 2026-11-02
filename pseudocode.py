# Boolean variables
card_valid = True
pin_correct = True
# Check the access card first
if card_valid:
    print("Access card accepted")
    # Check the PIN only if the card is valid
    if pin_correct:
        print("Access granted")
    else:
        print("Incorrect PIN")
else:
    print("Invalid access card")
