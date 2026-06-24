
def outer():
    
    print("This is Outer Function")

    def inner():
        print("This is Inner function")

    inner()
    print("Again Outer Function")
    inner()
    print("this is outer AGIAN")


print("Hello")
outer()
print("Bye")