

'''
  I need +,-,* and / results of 10 and 20
  for every operation you need to define functions with 2 arguments and every function must return value.
  add(no1,no2),sub(no1,no2),mul(no1,no2),div(no1,no2)
  ** One function need to call other function ....! and at last you call 1 function only. 

  I will call only 1 function, so that function need to call other and the function need to call next

  Ex :  add() <--> sub() <--> mul() <--> div()

'''

def add(no1,no2):
    return no1+no2

def sub(no1,no2):
    sum = add(no1,no2)
    print("Add = ",sum)
    return no1-no2

def mul(no1,no2):
    print("Sub = ",sub(no1,no2))
    return no1*no2

def div(no1,no2):
    print("Mul = ",mul(no1,no2))
    return no1/no2
    

print("Div = ",div(10,20))