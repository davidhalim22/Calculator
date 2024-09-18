firstnumber = float(input("1. Enter a number: "))
secondnumber = float(input("2. Enter a number: "))
operator = input("Enter a symbol for calculation (+,-,*,/): ")

def plus():
    answer = firstnumber + secondnumber
    print(f"Answer: {firstnumber} + {secondnumber} = {answer}")
    
def minus():
    answer = firstnumber - secondnumber
    print(f"Answer: {firstnumber} - {secondnumber} = {answer}")
    
def times():
    answer = firstnumber * secondnumber
    print(f"Answer: {firstnumber} * {secondnumber} = {answer}")
    
def divide():
    answer = firstnumber / secondnumber
    print(f"Answer: {firstnumber} / {secondnumber} = {answer}")

if operator == "+":
    plus()
elif operator == "-":
    minus()
elif operator == "*":
    times()
elif operator == "/":
    divide()
else:
    print("Error, Please Try Again!")