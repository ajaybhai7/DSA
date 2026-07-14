# Writing a program to calculate discount in an app

def calculate_discount(rupay):

    if rupay > 1000:
        naya_price = rupay - (rupay * 10 / 100)
    
    else:
        naya_price = rupay

    return naya_price
paise = int(input("Enter Amount: "))
discount = calculate_discount(paise)
print(f"Your Total Amount is : {discount}\nYou got discount : {paise} - {discount} = {(paise-discount)}")