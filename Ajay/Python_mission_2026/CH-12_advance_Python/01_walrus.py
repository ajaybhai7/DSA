# Using walrus operator

if (n := len([1, 3, 5, 3])) >3:
    print(f"List is too long ({n} elemtnts, expected <=3)")

# Output 