#1.write a function in python that takes a list of numbers and returns the sum of the given numbers. 

#2. write a function in python that takes a list of numbers and returns the second-largest item in the
# list of the given numbers. 

#3. write a function in python that takes 3 parameters: name, age, and occupation and prints this sentence
# as output: "My name is {name}, I am {age} years old and I work as a {occupation}". 

lst = [2,4, 5, 8, 10, 55, 20, 33]

def my_sum(lst):
    return sum(lst)

s = my_sum(lst)
print(s)

def second_largest(lst):
    lst.sort()
    return lst[-2]

m = second_largest(lst)
print(m)

def my_func(name, age, occupation):
    print(f'My name is {name}, I am {age}years old and I work as a {occupation}')
    
name = "Ian"
age = 30
occupation = "Doctor"

my_func(name, age, occupation)


   

