a = 90 # globle variable

def fun():
    global a # This will replace the global varible to local variable
    # means it shows Output 1
    a = 2

    print(a)

fun() #Local variable
print(a)

# Output 1
# 2
# 2
