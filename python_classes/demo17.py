
def outer():
    
    print("This is Outer Function")

    def inner():
        print("This is Inner function")

    print("Again Outer Function")


print("Hello")
outer()
print("Bye")