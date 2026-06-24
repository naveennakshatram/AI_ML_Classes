
def login(username,password):
    print("Welcome to Login page")
    if username == "naveen" and password == "kumar":
        return True
    return False



def balance_check(check_status):
    if check_status:
        return 10000
    return "Sorry please login"


print("Banking Application")
print("1. Login")
print("2. Check Balance")

status = login('naveen','kumar')

current_balacne = balance_check(status)
print(current_balacne)
