    # explore Lambda functions, map and reduce functions.
    # Look into python Lambda functions and any other func.
    # build multiple functions where return value of 1 func goes into 2nd function. and so on like 2-3-4 functions.
    # build a func to do the arithmetic operations on multiple argument inputs.
    # Do few examples on args and kwargs.

    # Learning Lambda : inline, short-lived logic, anonymous functions no name.

    # a normal function
# def square(x):
#     return x ** 2
# print(square(13))

    # same thing using lambda
# f = lambda x: x ** 2
# print(f(13))
    #or even directly use the function
# print((lambda x: x ** 2)(13))
    #we can pas multiple arguements as well and defaults as well
# Lam = lambda x,y,z=13:(x**2)+(y**3)+(z**4)
# print(Lam(2,3,4))
# print(Lam(3,4))
    #it supports conditional expressions as well (not statements)
# even = lambda x:"even" if x%2 == 0 else "odd"
# print(even(18))

# num = lambda x:"positive" if x > 0 else "negative" if x < 0 else "zero"
# print(num(5))
    #can return complex objetcs like tuples and dicts
# m = lambda x: (x,x**2,x**3)
# print(m(4))

# m = lambda name, age: {
#     "name": name,
#     "age": age,
#     "is_adult": age>=21
# }
# print(m("alex",12))

     #keyword arguements, basically when you dont want to pass parameters in a sequence (position-based) where the positions are predefined in the function creation
     #instrad you specify the order of parameter explicitly by also specifying the name of the parameter. instead of sum(2,3) we do sum(a=2,b=3)
     #the keyword "*" specifies that everything after this * will strictly only allow keyword arguments which needs the parameter name as well

# sum = lambda a,*,b:a+b
# print(sum(2,b=4))
# print(sum(b=2,4))  //throws an error

    #'*' is a seperator, we also have *args which acts as a collector of every parameter that comes after this
# sumOfNums = lambda x,*args : x + sum(args)
# print(sumOfNums(30,20,30,40,50))


    #map(): i used to use map for taking space sperated inputs into a complex object like a list
# nums = list(map(int,input("enter space seperated numbers: ").split()))
# print(nums)
    #you can define what the elements needs to be split by in the split function like default is " ",",","|" etc...
#     #syntax: map(fucniton, iterable)
# l = map(lambda x:x * 2,[2,3,4])
# print(l)
    #important: map is lazy iterator, it creates a map object not a list in the above code
# print(list(l))
    #this returns you a list [4,6,8] now the magic is its already exhausted
# print(list(l))
    #this returns an empty list [], meaning only once and then exhausted.

    #coming to REDUCERS(), suntax reduce(func,iterable,initializer = None), must have 2 arguements and initializer is optional
    #to use reduce, import from functools: from functools import reduce, it reduces an iterable by repeatedly applying the function on each element in the iterable,
# from functools import reduce
# red = reduce(lambda x,y: x+y,[2,3,4,5,6])
# print(red)
    #it first makes 2+3=5,5+4=9,9+5=14,14+6=20.
    #if there is an initializer
# red = reduce(lambda x,y: x+y,[2,3,4,5,6],50)
# print(red)
    #the execution starts with 50+2=52 and so on..
    #why init is imp -> if the list is empty [], returns a type error but if the list is empty [] and init exists as some value, the function returns that init value
# red = reduce(lambda x,y: x+y,[],50)
# print(red)
    #this is the safe way to do it in production environments


#build multiple functions where return value of 1 func goes into 2nd function. and so on like 2-3-4 functions.

# def clean(text):
#     text = text.strip().lower() #removing spaces and converting into lowercase
#     return tokenise(text)
# def tokenise(text):
#     words = text.split() #default it splits by space
#     return remove_shorts(words)
# def remove_shorts(words):
#     long_words = [_ for _ in words if len(_) > 3] #filters thriogh the list and removes short words
#     return count_words(long_words)
# def count_words(words):
#     return len(words) #just returns the count of long words in the list

# t = input("Enter a long sentence, use big words: ")
# result = count_words(remove_shorts(tokenise(clean(t))))
# result=clean(t)
# print(result)
#my input:   Respected your honor , iam DEEPLY disturbed by the fact that ironman died
#output: 9



# from functools import reduce

# def arithmetic(*numbers, operation="add"):
#     """Perform arithmetic on multiple numbers."""
#     if not numbers:
#         return None  # no numbers given
#     # Choose operation
#     if operation == "add":
#         func = lambda a, b: a + b
#     elif operation == "sub":
#         func = lambda a, b: a - b
#     elif operation == "mul":
#         func = lambda a, b: a * b
#     elif operation == "div":
#         func = lambda a, b: a / b
#     else:
#         raise ValueError("Invalid operation. Use 'add', 'sub', 'mul', or 'div'.")
#     # Apply the operation across all numbers
#     return reduce(func, numbers)
# result = arithmetic(10, 5, 2, operation="sub")
# print(result)



# *args and **kwargs
# def add_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# print(add_numbers(1, 2, 3))        # 6
# print(add_numbers(5, 10, 15, 20))  # 50
# print(add_numbers())               # 0


# using kwargs
# def greet(**kwargs):
#     for name, greeting in kwargs.items():
#         print(f"{greeting}, {name}!")
#
# # Call the function with keyword arguments
# greet(Alex="Hello", Maria="Hi", John="Good morning")

# f = map(lambda x:x%2 == 0,[1,2,3,4,5,6])
# print(list(f))

# f = filter(lambda x:x%2 == 0,[1,2,3,4,5,6])
# print(list(f))

# a = [1,2,3]
# b = [4,5,6]
#
# result = list(map(lambda x,y:x+y==7,a,b))
# print(result)

# r = map(lambda m:m+5,[85,88,90,92])
# res = filter(lambda m:m>90,r)
# print(list(res))