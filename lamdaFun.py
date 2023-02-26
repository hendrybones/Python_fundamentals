cube =lambda x : x * x *x
print(cube(7))

# list comprehension
a = [(lambda x: x * 2) (x) for x in range(6)]
print(a)


def greet(name):
    return  "hello  " + name
print(greet("hendry"))

numbers = [1, 2, 3, 4, 5 ]
squared_numbers= list(map(lambda x : x**2, numbers))
print(squared_numbers)
# the lambda function perform the operation to every element in the number llist

# example in filter
numbers = [1, 2, 3, 4, 5 ]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

num = 11
if((num % 2)==0 ):
    print("Even number")
else:
    print("odd number")

# odd numbers
for num in range(100):
    if num % 2 !=0:
        print(num,end=" ")
num = 11
if num > 1:
    for i in range(2, int(num/2)+ 1):
        if(num % i)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is prime number")
else:
    print(num,"not a prime number")


# how to use lambda fun to return functions as values
def make_order(x):
    return lambda y : x + y
add5= make_order(5)
print(add5(3))
# how to make lambda functions in sorting
numbers1 = [3,1,4,1,5,9,2,6,5,3,5]
sorted_number=sorted(numbers1, key=lambda x: +x)
print(sorted_number)

