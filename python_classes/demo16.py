
# how to change global variable value inside a function


# Global Variable
no1 = 100

def change_values():
    global no1
    no1 = 900  
    print("no1 value is ",no1)

print(no1)
change_values()
print(no1)