# Writing a program to calculate discount in an app

def calculate_discount(rupay):

    if rupay > 1000:
        naya_price = rupay - (rupay * 10 / 100)
    
    elif rupay <= 1000:
        naya_price = rupay

    return naya_price

discount = calculate_discount(rupay=int(input("Enter Total Amount: ")))
print(f"Your Total Discount is : {discount}")