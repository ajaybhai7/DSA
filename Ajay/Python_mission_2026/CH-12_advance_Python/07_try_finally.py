def main():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a Second number: "))
        print(f"The division is a/b is {a/b}")
        return
    except ValueError:
        print("Please Enter a Valid input!")
        return
    
    finally:
        print("==== End of the program ====")
    
main()


