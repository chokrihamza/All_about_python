def absolute_value(num):
    """This function returns the absolute value
    of an entred number """
    if num>0:
        return num
    else:
        return -num



print(absolute_value(-5))
print(absolute_value.__doc__)

# use lambda function in python
# higher order functions (function that takes in as argument other functions)
# as built in function we have filter() and map()

# let's start with the filter() function
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list=list(filter(lambda x:(x%2==0),my_list))
print(new_list)

# example with the function map()
# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)
