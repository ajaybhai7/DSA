# # Write a program to print largest number in the list

# def find_larger():
#     numbers = [10, 42, 5, 87, 23, 11]
    
#     # Maan lete hain ki pehla number hi sabse bada hai
#     largest = numbers[0]  

#     # List ke har number par ek-ek karke check karte hain
#     for x in numbers:
#         # Agar current number (x) humare 'largest' se bhi bada nikal gaya
#         if x > largest:
#             # Toh ab se 'largest' wahi current number (x) ban jayega
#             largest = x 
            
#     # Jab loop poori list ko check kar lega, tab hum final largest print karenge
#     print(f"Sabse bada number hai: {largest}")

# find_larger()


def find_larger():
    numbers = [1, 4, 6, 8, 2, 22, 2323, 6, 244]
    largest = numbers[0]

    for x in numbers:
        if x > largest:
            largest = x

    print(f"The largest number is : {largest}")

find_larger()
