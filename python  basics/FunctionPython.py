def ask_user():
    print("hello hendry")

# functions to return sum of number
def  my_func() :
    a = 0
    for i in range(1, 11):
        a = a + i
    return a
def student(firstname,lastname):
    print(firstname,lastname)
# keyword maintain the order of the parameters

student(firstname='hendry',lastname='mwamburi')
student(lastname='mwamburi',firstname='hendry')

# variable arguments
def myFun1(*argv):
    for arg in argv:
        print(arg,end=" ")

# variable keyword arguments
def myFun2(**kwargs):
    for key, value in kwargs.items():
        print("% s == % s" %(key, value))
# Driver Code
myFun1('Hello','Welcome','to','game')
print()
myFun2(first='hendry',mid='mkandoe',last='mwamburi')

# Calling functions
ask_user()
res = my_func()
print(res)


