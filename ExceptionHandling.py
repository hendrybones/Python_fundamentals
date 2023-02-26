def divide (x,y):
    try:
        result=x//y
        print("yeah ! your answer is ", result)
    except ZeroDivisionError:
        print("Sorry ! you are dividing by zero")

divide(2, 4)

# raise exception
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise
