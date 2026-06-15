
# Global Variable
no1 = 100

def change_values():
    no1 = 900  # Local variable
    print("no1 value is ",no1)

print(no1)
change_values()
print(no1)